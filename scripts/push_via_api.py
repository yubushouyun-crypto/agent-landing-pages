#!/usr/bin/env python3
"""
Push local files to GitHub via the API when git push is unreachable.

Usage:
    python3 scripts/push_via_api.py --file path/to/file:repo/path --file path/to/file2:repo/path2 \\
        --message "Commit message" \\
        --repo owner/repo --branch main

Requires:
    - GITHUB_TOKEN environment variable, or a token in the keychain at
      `security find-internet-password -s github.com -w`
    - Files must already exist at the specified local paths
"""

import json
import urllib.request
import base64
import subprocess
import sys
import os
import re


def get_token():
    """Try to get GitHub token from env, keychain, or gh config."""
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    if token:
        return token

    try:
        result = subprocess.run(
            ['security', 'find-internet-password', '-s', 'github.com', '-w'],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass

    # Check gh config
    gh_path = os.path.expanduser('~/.config/gh/hosts.yml')
    if os.path.exists(gh_path):
        with open(gh_path) as f:
            content = f.read()
            match = re.search(r'(?:oauth_token|token):\s*(\S+)', content)
            if match:
                return match.group(1)

    return None


def api_call(method, url, headers, data=None):
    """Make a GitHub API call."""
    req = urllib.request.Request(url, method=method, headers=headers, data=data)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def create_blob(token, repo, content):
    """Create a blob and return its SHA."""
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Hermes-Cron',
        'Content-Type': 'application/json'
    }
    body = json.dumps({
        'content': base64.b64encode(content.encode('utf-8')).decode('utf-8'),
        'encoding': 'base64'
    }).encode('utf-8')
    result = api_call('POST', f'https://api.github.com/repos/{repo}/git/blobs', headers, body)
    return result['sha']


def push(args):
    """Push files to GitHub via API."""
    repo = args.repo
    branch = args.branch or 'main'
    message = args.message or 'Automated push via API'

    token = get_token()
    if not token:
        print("ERROR: No GitHub token found.", file=sys.stderr)
        print("Set GITHUB_TOKEN env var or store in keychain.", file=sys.stderr)
        sys.exit(1)

    print(f"Token found ({token[:8]}...), repo={repo}, branch={branch}", file=sys.stderr)

    # Parse file mappings
    files = []
    for f in args.file:
        if ':' in f:
            local_path, repo_path = f.split(':', 1)
            files.append((local_path, repo_path))
        else:
            files.append((f, f))

    # Read file contents
    blobs = {}
    for local_path, repo_path in files:
        with open(local_path) as fh:
            content = fh.read()
        print(f"Creating blob for {repo_path}...", file=sys.stderr)
        sha = create_blob(token, repo, content)
        blobs[repo_path] = sha

    # Get latest commit ref
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Hermes-Cron'
    }
    ref = api_call('GET', f'https://api.github.com/repos/{repo}/git/refs/heads/{branch}', headers)
    latest_sha = ref['object']['sha']

    # Get base tree
    commit_data = api_call('GET', f'https://api.github.com/repos/{repo}/git/commits/{latest_sha}', headers)
    base_tree_sha = commit_data['tree']['sha']

    # Create tree
    tree_entries = [
        {'path': rp, 'mode': '100644', 'type': 'blob', 'sha': blobs[lp]}
        for lp, rp in files
    ]
    tree_body = json.dumps({
        'base_tree': base_tree_sha,
        'tree': tree_entries
    }).encode('utf-8')
    tree_result = api_call(
        'POST', f'https://api.github.com/repos/{repo}/git/trees',
        {**headers, 'Content-Type': 'application/json'}, tree_body
    )
    new_tree_sha = tree_result['sha']

    # Create commit
    commit_body = json.dumps({
        'message': message,
        'tree': new_tree_sha,
        'parents': [latest_sha]
    }).encode('utf-8')
    commit_result = api_call(
        'POST', f'https://api.github.com/repos/{repo}/git/commits',
        {**headers, 'Content-Type': 'application/json'}, commit_body
    )
    commit_sha = commit_result['sha']
    print(f"Created commit: {commit_sha[:12]}", file=sys.stderr)

    # Update ref
    ref_body = json.dumps({'sha': commit_sha}).encode('utf-8')
    api_call(
        'PATCH', f'https://api.github.com/repos/{repo}/git/refs/heads/{branch}',
        {**headers, 'Content-Type': 'application/json'}, ref_body
    )
    print(f"Branch {branch} updated. Push successful via API!", file=sys.stderr)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Push files to GitHub via API')
    parser.add_argument('--file', action='append', required=True,
                        help='local_path:repo_path (e.g., ./index.html:vidtrust/index.html)')
    parser.add_argument('--message', default='Automated push via API', help='Commit message')
    parser.add_argument('--repo', default='yubushouyun-crypto/agent-landing-pages', help='owner/repo')
    parser.add_argument('--branch', default='main', help='Branch name')
    args = parser.parse_args()
    push(args)

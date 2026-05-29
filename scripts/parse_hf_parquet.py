#!/usr/bin/env python3
"""
Parse the tech-news-daily parquet file from hf-mirror.com and output the latest
100 articles as JSON to stdout.

Usage:
    # After downloading the parquet file:
    python3 scripts/parse_hf_parquet.py

    # Or download + parse in one step:
    curl -s --max-time 120 -o /tmp/tech_news.parquet \
      "https://hf-mirror.com/datasets/shaurya03/tech-news-daily/resolve/refs%2Fconvert%2Fparquet/default/train/0000.parquet" \
      -L && python3 scripts/parse_hf_parquet.py
"""

import json
import sys
import subprocess
import os

PARQUET_PATH = os.path.expanduser('/tmp/tech_news.parquet')
PARQUET_URL = (
    "https://hf-mirror.com/datasets/shaurya03/tech-news-daily/"
    "resolve/refs%2Fconvert%2Fparquet/default/train/0000.parquet"
)


def ensure_deps():
    """Install required packages if missing."""
    required = ['fastparquet', 'numpy', 'pandas', 'packaging', 'cramjam', 'fsspec']
    missing = []
    for pkg in required:
        try:
            __import__(pkg.replace('-', '_'))
        except ImportError:
            missing.append(pkg)

    if missing:
        print(f"Installing missing dependencies: {', '.join(missing)}", file=sys.stderr)
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'install', '--quiet'] + missing,
            capture_output=True, text=True, timeout=300
        )
        if result.returncode != 0:
            print(f"Install failed: {result.stderr[-300:]}", file=sys.stderr)
            sys.exit(1)
        print("Dependencies installed.", file=sys.stderr)


def download_parquet():
    """Download parquet file if not already present."""
    if not os.path.exists(PARQUET_PATH) or os.path.getsize(PARQUET_PATH) < 1000000:
        print(f"Downloading parquet from hf-mirror...", file=sys.stderr)
        result = subprocess.run(
            ['curl', '-s', '--max-time', '120', '-o', PARQUET_PATH, PARQUET_URL, '-L'],
            capture_output=True, text=True, timeout=180
        )
        if result.returncode != 0:
            print(f"Download failed: {result.returncode}", file=sys.stderr)
            sys.exit(1)
        size_mb = os.path.getsize(PARQUET_PATH) / 1024 / 1024
        print(f"Downloaded {size_mb:.1f} MB", file=sys.stderr)
    else:
        print(f"Using cached parquet ({os.path.getsize(PARQUET_PATH) / 1024 / 1024:.1f} MB)", file=sys.stderr)


def parse_and_output():
    """Parse parquet and output latest 100 rows as JSON."""
    import fastparquet as fp

    pf = fp.ParquetFile(PARQUET_PATH)
    total_rows = pf.info['rows']
    print(f"Total rows: {total_rows}, Columns: {pf.info['columns']}", file=sys.stderr)

    df = pf.to_pandas()

    # Sort by published date descending
    if 'published' in df.columns:
        df_sorted = df.sort_values('published', ascending=False)
    else:
        df_sorted = df.iloc[::-1]  # reverse if no date column

    latest = df_sorted.head(100).to_dict(orient='records')

    result = {
        "num_rows_total": total_rows,
        "columns": list(df.columns),
        "rows": latest
    }

    print(json.dumps(result, ensure_ascii=False, default=str))


if __name__ == '__main__':
    ensure_deps()
    download_parquet()
    parse_and_output()

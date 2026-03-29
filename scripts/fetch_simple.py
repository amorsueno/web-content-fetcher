#!/usr/bin/env python3
"""
简化版网页正文提取脚本（基于 html2text + urllib）
无需 scrapling，适用于基本网页提取
"""

import sys
import re
import html2text
from urllib.request import Request, urlopen
from urllib.error import HTTPError


def fetch_url(url):
    """获取网页内容"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.google.com/"
    }
    
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=30) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error fetching {url}: {e}"


def html_to_markdown(html, max_chars=30000):
    """将 HTML 转换为 Markdown"""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # 不自动换行
    
    md = h.handle(html)
    md = re.sub(r'\n{3,}', '\n\n', md).strip()
    return md[:max_chars]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python3 fetch_simple.py <url> [max_chars]", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    max_chars = int(sys.argv[2]) if len(sys.argv) > 2 else 30000

    html = fetch_url(url)
    if html.startswith("Error"):
        print(html, file=sys.stderr)
        sys.exit(1)
    
    md = html_to_markdown(html, max_chars)
    print(md)

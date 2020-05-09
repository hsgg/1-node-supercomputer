#!/usr/bin/env python3

from markdown2 import markdown_path

top = """<!DOCTYPE html>
<html>
"""

bottom = """
</html>
"""


def md2html(path):
    # head
    with open("snippets/head.html", "r") as f:
        head = f.read()

    # body
    body = "\n".join(["<body>", markdown_path(path), "</body>"])

    # full html
    html = "\n".join([top, head, body, bottom])
    return html


def main():
    html = md2html("test/blog.md")
    print(html)

main()

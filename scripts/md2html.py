#!/usr/bin/env python3

import os
from markdown2 import markdown_path

top = """<!DOCTYPE html>
<html>
"""

bottom = """
</html>
"""

mdfiles = [
        "../2017/blog-20170520.md",
        "../2017/blog-20170604.md",
        "../2017/blog-20170605.md",
        "../2017/blog-20170614.md",
        "../2017/thingsnobodycaresaboutbutme.md",
        "../2018/blog-20180101.md",
        "../2018/blog-20180118.md",
        "../2018/blog-20180326.md",
        "../2018/blog-20180516.md",
        "../2018/blog-20180601.md",
        "../2018/blog-20181121.md",
        "../2019/blog-20190324.md",
        "../2020/blog-20200426.md",
        ]


def readfile(path):
    with open(path, "r") as f:
        contents = f.read()
    return contents


def writefile(path, contents):
    with open(path, "w") as f:
        f.write(contents)


head = readfile("snippets/head.html")
footer = readfile("snippets/footer.html")

def md2html(path):
    body = "\n".join(["<body>", markdown_path(path), "</body>"])
    html = "\n".join([top, head, body, footer, bottom])
    return html


def main():
    # convert md files to html
    for mdfile in mdfiles:
        htmlfile = ".".join([os.path.splitext(mdfile)[0], "html"])
        print("Converting", mdfile, "->", htmlfile, "...")
        html = md2html(mdfile)
        writefile(htmlfile, html)

main()

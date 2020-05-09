#!/usr/bin/env python3

import os
from markdown2 import markdown, markdown_path

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
        "../2018/blog-20180101.md",
        "../2018/blog-20180118.md",
        "../2018/blog-20180326.md",
        "../2018/blog-20180516.md",
        "../2018/blog-20180601.md",
        "../2018/blog-20181121.md",
        "../2019/blog-20190324.md",
        "../2020/blog-20200426.md",
        "../2017/thingsnobodycaresaboutbutme.md",
        ]


def readfile(path):
    with open(path, "r") as f:
        contents = f.read()
    return contents


def writefile(path, contents):
    with open(path, "w") as f:
        f.write(contents)


def readfirstline(path):
    with open(path, "r") as f:
        line = f.readline()
    return line


def path_md2html(mdfile):
    htmlfile = ".".join([os.path.splitext(mdfile)[0], "html"])
    return htmlfile


def main():
    head = readfile("snippets/head.html")
    footer = readfile("snippets/footer.html")

    # convert md files to html
    for mdfile in mdfiles:
        htmlfile = path_md2html(mdfile)
        print("Converting", mdfile, "->", htmlfile, "...")
        body = "\n".join(["<body>", markdown_path(mdfile), "</body>"])
        html = "\n".join([top, head, body, footer, bottom])
        writefile(htmlfile, html)

    # generate index.html
    indexpre = markdown_path("snippets/index-pre.html")
    toc = ""
    for mdfile in mdfiles:
        htmlfile = path_md2html(mdfile)
        date = mdfile[13:-3]
        title = date[:4] + "-" + date[4:6] + "-" + date[6:] + ": "
        if len(title) != 12:
            title = ""
        title += readfirstline(mdfile)[2:-1]
        print(title)
        toc += "\n  - [" + title + "](" + htmlfile + ")"
    # other entries
    toc += "\n  - [Shue's blog](../2018/shuesblog/)"
    toc = markdown(toc)
    html = "\n".join([top, head, "<body>", indexpre, toc, "</body>", footer, bottom])
    writefile("../2020/index.html", html)

main()

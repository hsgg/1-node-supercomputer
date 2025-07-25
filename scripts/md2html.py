#!/usr/bin/env python3

import os
import sys

#import markdown2

#import markdown

#from cmarkgfm import markdown_to_html
#import cmarkgfm
#from cmarkgfm import markdown_to_html_with_extensions

import pypandoc



def markdown(md):
    #extensions = ["footnotes", "strike", "tables"]
    #extensions = ["extra", "strike", "tables"]
    #return markdown2.markdown(md, extras=extensions)

    #opts = (cmarkgfm.cmark.Options.CMARK_OPT_UNSAFE
    #        | cmarkgfm.cmark.Options.CMARK_OPT_FOOTNOTES)
    #return markdown_to_html_with_extensions(md, options=opts)

    s = pypandoc.convert_text(md, to='html', format='md', extra_args=['--mathml'])
    return s


# load markdown from file `fname`, then convert to html
def markdown_path(fname):
    with open(fname, "r") as f:
        md = f.read()
    html = markdown(md)
    return html



script_dir = os.path.dirname(os.path.abspath(__file__))

top = """<!DOCTYPE html>
<html>
"""

bottom = """
</html>
"""

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


def ismarkdownfile(fname):
    exists = os.path.isfile(fname)
    ext = os.path.splitext(fname)[1]
    return ext == ".md" and exists


def path_md2html(mdfile):
    htmlfile = ".".join([os.path.splitext(mdfile)[0], "html"])
    return htmlfile


def mdfile_date(mdfile, postfix=""):
    fname = os.path.splitext(os.path.basename(mdfile))[0]
    s = fname.split('-')
    if len(s) < 2:
        return ""
    date = s[1]
    date = date[:4] + "-" + date[4:6] + "-" + date[6:]
    if len(date) != 10:
        return ""
    else:
        return date + postfix


def get_title_from_filename(fname, postfix=""):
    fname = os.path.splitext(os.path.basename(fname))[0]
    s = fname.split('-')
    if len(s) < 2:
        return ""
    date = s[1]
    date = date[:4] + "-" + date[4:6] + "-" + date[6:]
    if len(date) != 10:
        return ""
    title = date + ": " + " ".join(s[2:])
    return title + postfix



def encapsulate(env, content, **properties):
    prop = ""
    for p in properties:
        prop += " "
        prop += p + "=" + properties[p]
    s = "<" + env + prop + ">" + content + "</" + env + ">"
    return s


def convert_single_file(mdfile):
    if not ismarkdownfile(mdfile):
        print(f"Nothing to convert: {mdfile}")
        return
    htmlfile = path_md2html(mdfile)
    print("Converting", mdfile, "->", htmlfile, "...")
    head = readfile(f"{script_dir}/snippets/head.html")
    date = mdfile_date(mdfile)
    date = encapsulate("span", date, style="float:right;")
    home = encapsulate("a", "2-node-supercomputer.net", href="http://2-node-supercomputer.net")
    home = encapsulate("em", home)
    banner = encapsulate("p", home + "\n" + date, style="text-align:left;")
    footer = encapsulate("footer", banner)
    html = "\n".join([
        top,
        head,
        "<body>",
        banner + "\n",
        markdown_path(mdfile),
        footer + "\n",
        "</body>\n",
        bottom])
    writefile(htmlfile, html)


def create_index(mdfile, mdfile_list):
    htmlfile = path_md2html(mdfile)

    print("Creating index", mdfile, "->", htmlfile, "...")

    indexpre = markdown_path(mdfile)
    toc = "## Contents\n"
    for blog_mdfile in mdfile_list:
        blog_htmlfile = path_md2html(blog_mdfile)
        if ismarkdownfile(blog_mdfile):
            title = mdfile_date(blog_mdfile, ": ") + readfirstline(blog_mdfile)[2:-1]
        else:
            title = get_title_from_filename(blog_htmlfile)
        print(title)
        if not os.path.exists(blog_htmlfile):
            raise FileNotFoundError(blog_htmlfile)
        toc += "\n  - [" + title + "](../" + blog_htmlfile + ")"

    head = readfile(f"{script_dir}/snippets/head.html")
    toc = markdown(toc)
    footer = encapsulate("a", "2-node-supercomputer.net", href="http://2-node-supercomputer.net")
    footer = encapsulate("em", footer)
    footer = encapsulate("p", footer, style="text-align:center;")
    footer = encapsulate("footer", footer)
    html = "\n".join([
        top,
        head,
        "<body>",
        indexpre,
        toc,
        footer + "\n",
        "</body>",
        bottom])

    writefile(htmlfile, html)


def main():
    if sys.argv[1] == "-h":
        print(f"Usage: {sys.argv[0]} [-i index.md] <file1.md> [file2.md...]")
        return

    if sys.argv[1] == "-i":
        index_mdfile = sys.argv[2]
        mdfile_list = sys.argv[3:]
        create_index(index_mdfile, mdfile_list)
        return

    for mdfile in sys.argv[1:]:
        convert_single_file(mdfile)


main()

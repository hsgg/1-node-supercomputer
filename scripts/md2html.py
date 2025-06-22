#!/usr/bin/env python3

import os

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



os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
        "../2020/blog-20200523.md",
        "../2020/blog-20200531.md",
        "../2020/blog-20200621.md",
        "../2020/blog-20200704.md",
        "../2020/blog-20200713-is-the-US-outspending-itself.md",
        "../2026/blog-20200724-future-mars-boarding-pass.md",
        "../2020/blog-20200728-cpu-operation-costs.md",
        "../2020/blog-20200731-gdb-signals.md",
        "../2020/blog-20200809-read-more-see-all.md",
        "../2020/blog-20200810-googleplusdatalitigation.md",
        "../2020/blog-20201025-campaign-fundraising.md",
        "../2020/blog-20201114-evince-link-preview.md",
        "../2020/blog-20201211-dark-mode.md",
        "../2021/blog-20210324-my-spam-gets-more-attention.md",
        "../2021/blog-20210508-science-quantifies-uncertainty.md",
        "../2021/blog-20210611-matplotlib-imshow-none-nearest.md",
        "../2021/blog-20210614-escaping-the-bubble.md",
        "../2021/blog-20210717-housing-prices-as-a-proxy.md",
        "../2021/blog-20210805-Vaccines-vs-Covid.html",
        "../2021/blog-20210810-artgerecht.md",
        "../2021/blog-20210827-ipv6.md",
        "../2021/blog-20211029-optimize-for-signal.md",
        "../2022/blog-20220202-forms.md",
        "../2022/blog-20220315-dst.md",
        "../2022/blog-20220320-taxes.md",
        "../2022/blog-20220409-inflation-is-fair.md",
        "../2022/blog-20220427-voter-suppression-vs-election-integrity.md",
        "../2022/blog-20220507-mentoring-students.md",
        "../2022/blog-20220508-hsr-texas-benefits-from-california.md",
        "../2022/blog-20220802-reduce.md",
        "../2022/blog-20220905-inflation-is-accurate.md",
        "../2022/blog-20221029-zero-sum-vs-win-win.md",
        "../2023/blog-20230103-closed-loop-hydro-storage.md",
        "../2023/blog-20230108-bad-documentaries.md",
        "../2023/blog-20230119-worst-infographic-ever.md",
        "../2023/blog-20230315-inotifywait.md",
        "../2023/blog-20230327-julias-update-mania.md",
        "../2023/blog-20230412-organic-tea-is-responsible-for-hunger.md",
        "../2023/blog-20230512-sodimm-speed-and-latency.md",
        "../2023/blog-20231021-substitution.md",
        "../2024/blog-20240109-git-fast-forward.md",
        "../2024/blog-20240124-dual-seat-xorg.md",
        "../2024/blog-20240126-the-main-dev-anti-pattern.md",
        "../2024/blog-20240509-gitk-on-mac.md",
        "../2024/blog-20241003-reproducible-and-updatable-science.md",
        "../2025/blog-20250223-choosing-a-license.md",
        "../2025/blog-20250531-degenerate-gaussian.md",
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


def ismarkdownfile(fname):
    ext = os.path.splitext(fname)[1]
    return ext == ".md"


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


def main():
    head = readfile("snippets/head.html")

    # convert md files to html
    for mdfile in mdfiles:
        if not ismarkdownfile(mdfile):
            continue
        htmlfile = path_md2html(mdfile)
        print("Converting", mdfile, "->", htmlfile, "...")
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

    # generate index.html
    indexpre = markdown_path("../2025/index.md")
    toc = "## Contents\n"
    for mdfile in mdfiles:
        if ismarkdownfile(mdfile):
            htmlfile = path_md2html(mdfile)
            title = mdfile_date(mdfile, ": ") + readfirstline(mdfile)[2:-1]
        else:
            htmlfile = mdfile
            title = get_title_from_filename(htmlfile)
        print(title)
        if not os.path.exists(htmlfile):
            raise FileNotFoundError(htmlfile)
        toc += "\n  - [" + title + "](" + htmlfile + ")"

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
    writefile("../2025/index.html", html)

main()

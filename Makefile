INDEX_HTML_FILE = 2025/index.html
INDEX_MD_FILE = $(subst .html,.md,$(INDEX_HTML_FILE))

BLOG_HTML_FILES += 2017/blog-20170520.html
BLOG_HTML_FILES += 2017/blog-20170604.html
BLOG_HTML_FILES += 2017/blog-20170605.html
BLOG_HTML_FILES += 2017/blog-20170614.html
BLOG_HTML_FILES += 2018/blog-20180101.html
BLOG_HTML_FILES += 2018/blog-20180118.html
BLOG_HTML_FILES += 2018/blog-20180326.html
BLOG_HTML_FILES += 2018/blog-20180516.html
BLOG_HTML_FILES += 2018/blog-20180601.html
BLOG_HTML_FILES += 2018/blog-20181121.html
BLOG_HTML_FILES += 2019/blog-20190324.html
BLOG_HTML_FILES += 2020/blog-20200426.html
BLOG_HTML_FILES += 2020/blog-20200523.html
BLOG_HTML_FILES += 2020/blog-20200531.html
BLOG_HTML_FILES += 2020/blog-20200621.html
BLOG_HTML_FILES += 2020/blog-20200704.html
BLOG_HTML_FILES += 2020/blog-20200713-is-the-US-outspending-itself.html
BLOG_HTML_FILES += 2026/blog-20200724-future-mars-boarding-pass.html
BLOG_HTML_FILES += 2020/blog-20200728-cpu-operation-costs.html
BLOG_HTML_FILES += 2020/blog-20200731-gdb-signals.html
BLOG_HTML_FILES += 2020/blog-20200809-read-more-see-all.html
BLOG_HTML_FILES += 2020/blog-20200810-googleplusdatalitigation.html
BLOG_HTML_FILES += 2020/blog-20201025-campaign-fundraising.html
BLOG_HTML_FILES += 2020/blog-20201114-evince-link-preview.html
BLOG_HTML_FILES += 2020/blog-20201211-dark-mode.html
BLOG_HTML_FILES += 2021/blog-20210324-my-spam-gets-more-attention.html
BLOG_HTML_FILES += 2021/blog-20210508-science-quantifies-uncertainty.html
BLOG_HTML_FILES += 2021/blog-20210611-matplotlib-imshow-none-nearest.html
BLOG_HTML_FILES += 2021/blog-20210614-escaping-the-bubble.html
BLOG_HTML_FILES += 2021/blog-20210717-housing-prices-as-a-proxy.html
BLOG_HTML_FILES += 2021/blog-20210805-Vaccines-vs-Covid.html
BLOG_HTML_FILES += 2021/blog-20210810-artgerecht.html
BLOG_HTML_FILES += 2021/blog-20210827-ipv6.html
BLOG_HTML_FILES += 2021/blog-20211029-optimize-for-signal.html
BLOG_HTML_FILES += 2022/blog-20220202-forms.html
BLOG_HTML_FILES += 2022/blog-20220315-dst.html
BLOG_HTML_FILES += 2022/blog-20220320-taxes.html
BLOG_HTML_FILES += 2022/blog-20220409-inflation-is-fair.html
BLOG_HTML_FILES += 2022/blog-20220427-voter-suppression-vs-election-integrity.html
BLOG_HTML_FILES += 2022/blog-20220507-mentoring-students.html
BLOG_HTML_FILES += 2022/blog-20220508-hsr-texas-benefits-from-california.html
BLOG_HTML_FILES += 2022/blog-20220802-reduce.html
BLOG_HTML_FILES += 2022/blog-20220905-inflation-is-accurate.html
BLOG_HTML_FILES += 2022/blog-20221029-zero-sum-vs-win-win.html
BLOG_HTML_FILES += 2023/blog-20230103-closed-loop-hydro-storage.html
BLOG_HTML_FILES += 2023/blog-20230108-bad-documentaries.html
BLOG_HTML_FILES += 2023/blog-20230119-worst-infographic-ever.html
BLOG_HTML_FILES += 2023/blog-20230315-inotifywait.html
BLOG_HTML_FILES += 2023/blog-20230327-julias-update-mania.html
BLOG_HTML_FILES += 2023/blog-20230412-organic-tea-is-responsible-for-hunger.html
BLOG_HTML_FILES += 2023/blog-20230512-sodimm-speed-and-latency.html
BLOG_HTML_FILES += 2023/blog-20231021-substitution.html
BLOG_HTML_FILES += 2024/blog-20240109-git-fast-forward.html
BLOG_HTML_FILES += 2024/blog-20240124-dual-seat-xorg.html
BLOG_HTML_FILES += 2024/blog-20240126-the-main-dev-anti-pattern.html
BLOG_HTML_FILES += 2024/blog-20240509-gitk-on-mac.html
BLOG_HTML_FILES += 2024/blog-20241003-reproducible-and-updatable-science.html
BLOG_HTML_FILES += 2025/blog-20250223-choosing-a-license.html
BLOG_HTML_FILES += 2025/blog-20250531-degenerate-gaussian.html
BLOG_HTML_FILES += 2017/thingsnobodycaresaboutbutme.html

BLOG_MD_FILES = $(subst .html,.md,$(BLOG_HTML_FILES))

all: $(INDEX_HTML_FILE) $(BLOG_HTML_FILES)

$(INDEX_HTML_FILE): $(INDEX_MD_FILE) $(BLOG_HTML_FILES) $(BLOG_MD_FILES)
	@./scripts/md2html.py -i $< $(BLOG_MD_FILES)

%.html: %.md
	@./scripts/md2html.py $<


# Not everything is generated from a .md file. List them here.
# Note: This approach leads to the index being rebuilt every time make is run.
# I think that is OK.
.PHONY: 2021/blog-20210805-Vaccines-vs-Covid.md

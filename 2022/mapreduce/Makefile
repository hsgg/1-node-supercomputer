all: mapreduce.svg

%.svg: %.pdf
	pdftocairo -svg $<

%.pdf: %.tex
	latexmk -pdf $<

all: runscript

runscript: mapreduce/all
	../scripts/md2html.py

push:
	../scripts/upload.sh


mapreduce/all:
	$(MAKE) -C mapreduce

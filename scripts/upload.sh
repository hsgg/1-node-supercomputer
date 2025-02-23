#!/bin/sh

git push && ssh 2-node-www 'su - hsgg -c "cd 1-node-supercomputer; git pull"'

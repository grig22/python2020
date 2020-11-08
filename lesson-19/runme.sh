#!/bin/bash
if [[ -f $1 ]]; then
	./parser.py "$1"
elif [[ -d $1 ]]; then
	bash -O extglob -c "./parser.py $1/access.log?(.+([[:alnum:]]))"
fi

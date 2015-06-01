#!/usr/bin/python

## rot13.py version 0.1 - Replace each letter with the 13th letter after it (c)gfragkos 2014  ##
## It can to ROT13 to a given text either through a pipe or as an argument from stdin.        ##
## You may modify, reuse and distribute the code freely as long as it is referenced back      ##
## to the author using the following line: ..based on rot13.py by @drgfragkos                 ##

import sys

if len(sys.argv) != 2:    ## If no argument given, read from pipe
	line = sys.stdin.readline()
	line = line.rstrip('\n')   ## readline() includes a \n, needs to be removed
	line = line.strip()
	print line.encode("rot_13")  
	exit(0);

else:
	phrase = sys.argv[1]  ## When argument is given
	phrase = phrase.rstrip('\n')
	phrase = phrase.strip()
	print phrase.encode("rot_13")





#!/bin/sh

cut -f 1 tmp/hightemp.txt | sort | uniq -c | sort --reverse

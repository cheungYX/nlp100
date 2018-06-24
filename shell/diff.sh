#!/bin/sh

cut -f 1 tmp/hightemp.txt | sort | uniq > tmp/result.txt

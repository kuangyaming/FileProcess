#!/usr/bin/python

import sys
import argparse
import os.path

parser = argparse.ArgumentParser(description="Caculate count and sum of float numbers in a given file")
parser.add_argument("filepath", help="file path which stores lines of float numbers")
args = parser.parse_args()

filepath = args.filepath

if not os.path.isfile(filepath):
    parser.print_help()
    exit()

f = open (filepath, 'r')
out = f.readlines()

numCount = 0
Sum = 0
for line in out:
    words = line.split()
    numCount += len(words)
    for word in words:
        try: 
            Sum += float(word)
        except:
            #skip this non-float element
            continue

print numCount
print Sum

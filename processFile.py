#!/usr/bin/python

# File Create Date:
#   Nov. 8th, 2015
#
# Name: Kuang Yaming

import sys
import argparse
import os.path

# 
# Description:
#   Set up parameter and program description
#   If not enough parameters are provided, error message and help message will be printed out.
#   Validation of the file path is not handled in this sub routine. 
#
# Input:
#   None
#
# Output:
#   file path 
#
def parseParam ():
    parser = argparse.ArgumentParser(description="Caculate count and sum of float numbers in a given file")
    parser.add_argument("filepath", help="file path which stores lines of float numbers")
    args = parser.parse_args()

    # Get file path
    return args.filepath

# 
# Description:
#   Check the validation of given file path
#
# Input:
#   file path
#
# Output:
#   True  : if the file path is valid.
#   False : if the file path is invalid.
#
def checkFile(filepath):
    if not os.path.isfile(filepath):
        print "Invalid file path. Pls input valid file path."
        parser.print_help()
        return False
    else:
        return True

# 
# Description:
#   1. Read file line by line.
#   2. Split line into strings separated by white spaces.
#   3. Convert string into float. 
#   4. If this is a valid float number, sum up.
#      If not, skip this string and continue processing other string.
#      If this is the last string in this line, go back to step #1.
#   5. If this is the last line, print out "Total Float Elements" and "Sum".
#
# Input:
#   file path
#
# Output:
#   None.
#   Totoal Float Elements and Sum will be printed out.
#
def processFile(filepath):
    if True != checkFile (filepath):
        exit()

    f = open (filepath, 'r')
    out = f.readlines()

    numCount = 0
    Sum = 0
    for line in out:
        words = line.split()
        for word in words:
            try: 
                Sum += float(word)
                numCount += 1
            except:
                #skip this non-float element
                continue

    print "Total Float Elements: %s" % numCount
    print "Sum: %s" % Sum

filepath = parseParam()
processFile(filepath)

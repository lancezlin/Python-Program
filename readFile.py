# -*- coding: utf-8 -*-
"""
Write a program to read through a file and print the contents of the
file (line by line) all in upper case.
@author: lancezlin
"""

fname = raw_input('Type a file name to read: \n')
try:
    openFile = open(fname)
    for line in openFile:
        line = line.upper().rstrip().lstrip()
        print line
except:
    print 'File cannot be opened!'
    exit()


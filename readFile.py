# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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


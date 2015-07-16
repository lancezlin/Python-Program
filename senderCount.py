# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:51:30 2015
Write a program to read through the mail box data and when you
find line that starts with “From”, you will split the line into words using the split
function. We are interested in who sent the message which is the second word on
the From line.
@author: linla
"""

inp = raw_input('Please enter a file name to open:\n')
try:
    fileName = open(inp)
    senderList = list()
    for line in fileName:
        line.rstrip().lstrip()
        if line.startswith('From'):
            words = line.split()
            senderList.append(words[1])
        else:
            continue
    print senderList
    print len(senderList)
except:
    print 'cannot open %s.' % inp

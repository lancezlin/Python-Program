# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:36:56 2015
Write a program to read through a mail log, and build a histogram
using a dictionary to count how many messages have come from each email address
and print the dictionary.
@author: linla
"""

inp = raw_input('please enter a file name to opne:\n')
try:
    fileName = open(inp)
except:
    print 'Cannot open %s.' % inp
    
emailCount = dict()
for line in fileName:
    line = line.rstrip().lstrip()
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2:
            emailAddress = words[1]
            emailCount[emailAddress] = emailCount.get(emailAddress, 0) + 1
        else:
            continue
    else:
        continue
print emailCount

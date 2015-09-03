# -*- coding: utf-8 -*-
# Author: lance
"""
Created on Thu Jul 16 15:18:55 2015
Write a program that categorizes each mail message by which day of
the week the commit was done. To do this look for lines which start with “From”,
then look for the third word and then keep a running count of each of the days
of the week. At the end of the program print out the contents of your dictionary
@author: linla
"""

inp = raw_input('please enter a file name to open:\n')
try:
    fileName = open(inp)
except:
    print 'Cannot open %s.' % inp
dayDic = dict()    
for line in fileName:
    line = line.rstrip().lstrip()
    if not line.startswith('From'):
        continue
    else:
        words = line.split()
        if len(words) < 3:
            continue
        else:
            word = words[2]
            dayDic[word] = dayDic.get(word, 0) + 1
print dayDic

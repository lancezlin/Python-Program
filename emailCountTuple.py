# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:00:06 2015

@author: Lance
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

emailList = list()
for key, val in emailCount.items():
    emailList.append((val, key))

emailList.sort(reverse = True)
print emailList[: 1]

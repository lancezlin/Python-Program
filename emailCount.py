# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:36:56 2015
Write a program to read through a mail log, and build a histogram
using a dictionary to count how many messages have come from each email address
and print the dictionary.
Add code to the above program to figure out who has the most messages
in the file.
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
# point out who sent most messages:
largest = None
for eml in emailCount.keys():
    if emailCount[eml] > largest:
        largest= emailCount[eml]
        continue
    else:
        largest = largest
print emailCount.keys()[emailCount.values().index(largest)], largest
'''
def maxEmail(Dic):
    largest = None
    for emails in Dic.keys():
        if Dic[emails] > largest:
            largest= Dic[emails]
            continue
        else:
            largest = largest
    return largest

print maxEmail(emailCount)
'''

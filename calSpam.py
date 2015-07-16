# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:40:33 2015

@author: Lance
"""

fileName = raw_input('Please type a file name here: \n')
try:
    openFile = open(fileName)
    count = 0
    total = 0
    avgSpam = None
    for line in openFile:
        line.rstrip().lstrip()
        if line.startswith('X-DSPAM-Confidence:'):
            startPoint = line.find(':')
            endPoint = len(line)
            spams = line[startPoint+2:endPoint]
            count = count + 1
            total = total + float(spams)
            avgSpam = total/count
        else:
            continue
    print count, total, avgSpam
except:
    print 'Cannot open the file'

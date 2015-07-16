# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:40:33 2015
Write a program to prompt for a file name, and then read through
the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
the line to extract the floating point number on the line. Count these lines and the
compute the total of the spam confidence values from these lines. When you reach
the end of the file, print out the average spam confidence.
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

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:31:28 2015
Write a program to open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word is not in the
list, add it to the list.
When the program completes, sort and print the resulting words in alphabetical
order.
@author: linla
"""

inp = raw_input('please enter a file name here: \n')
try:
    fileName = open(inp)
    uniqWord = list()
    for line in fileName:
        words= line.split()
        for word in words:
            if word not in uniqWord:
                uniqWord.append(word)
                uniqWord.sort(key=str.lower)
            else:
                continue
    #uniqWord.sort()
    print uniqWord
except:
    print 'cannot find %s.' % inp    

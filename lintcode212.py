# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:10:40 2015
Write a method to replace all spaces in a string with %20. The string is given 
in a characters array, you can assume it has enough space for replacement and 
you are given the true length of the string.

Example
Given "Mr John Smith", length = 13.

The string after replacement should be "Mr%20John%20Smith".
@author: linla
"""
string = raw_input('Enter a string:\n')
try:
    string = str(string)
except:
    'it is not a string'

newStr = str()
lg = len(string)
if lg >0:
    for i in range(0,lg):
        if string[i]!=' ':
            newStr = newStr + string[i]
        else:
            newStr = newStr + '%20'
            continue
        length = len(newStr)
    print newStr

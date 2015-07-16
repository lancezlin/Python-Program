# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:32:47 2015
Rewrite the program that prompts the user for a list of numbers and
prints out the maximum and minimum of the numbers at the end when the user
enters “done”. Write the program to store the numbers the user enters in a list
and use the max() and min() functions to compute the maximum and minimum
numbers after the loop completes.
@author: linla
"""


numList = list()
while True:
    inp = raw_input('Please enter a number: \n')
    try:
        value = float(inp)
        numList.append(value)
    except:
        if inp == 'done':
            if len(numList) < 1:
                print 'It is not done! please enter a number.'
                continue
            else:
                break
        else:
            print 'Invalid Value! Please reenter a number.'
            continue
print max(numList), min(numList)

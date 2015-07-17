# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:16:10 2015

@author: Lance
"""

inp = raw_input('please enter a file name:\n')
try:
    fname = open(inp)
except:
    print 'Cannot open %s.' % inp

hrCount = dict()
for line in fname:
    line = line.rstrip().lstrip()
    if line.startswith('From'):
        words = line.split()
        if len(words) >= 6:
            tm = words[5].split(':')
            hr = tm[0]
            hrCount[hr] = hrCount.get(hr, 0) + 1
        else:
            continue
    else:
        continue

hrList = list()
for key, val in hrCount.items():
    hrList.append((val, key))

hrList.sort(reverse = True)
print hrList

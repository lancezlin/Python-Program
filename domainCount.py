# -*- coding: utf-8 -*-
"""
This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from (i.e. the
whole e-mail address). At the end of the program print out the contents of your
dictionary.
@author: linla
"""

inp = raw_input('please enter a file name to opne:\n')
try:
    fileName = open(inp)
except:
    print 'Cannot open %s.' % inp
    
domainCount = dict()
for line in fileName:
    line = line.rstrip().lstrip()
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2:
            emailAddress = words[1]
            stPoint = emailAddress.find('@')
            endPoint = len(emailAddress)
            domainName = emailAddress[stPoint+1:endPoint]
            domainCount[domainName] = domainCount.get(domainName, 0) + 1
        else:
            continue
    else:
        continue
print domainCount

largest = None
for dom in domainCount.keys():
    if domainCount[dom] > largest:
        largest= domainCount[dom]
        continue
    else:
        largest = largest
print domainCount.keys()[domainCount.values().index(largest)], largest

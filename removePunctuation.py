# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:52:09 2015

@author: Lance
"""

# Capitalization and punctuation removing function
import re
def removePunctuation(text):
    return re.sub(r'[a-zA-Z0-9\s]+', '', text).lower().strip()

print removePunctuation('u= what')
print removePunctuation(' hello world ! ')

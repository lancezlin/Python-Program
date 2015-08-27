# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 22:28:55 2015

@author: Lance
"""

def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startwith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

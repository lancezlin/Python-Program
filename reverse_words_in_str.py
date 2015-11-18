# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:05:17 2015
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
@author: Lance
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([word[::-1] for word in s[::-1].split()])
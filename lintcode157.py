'''
Implement an algorithm to determine if a string has all unique characters.

Example:
Given "abc", return true.

Given "aab", return false.
'''

class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        if len(str) <= 1:
            return True
        else:
            for char in str:
                if str.count(char) >= 2:
                    return False
        return True

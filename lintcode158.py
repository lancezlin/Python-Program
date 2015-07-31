'''
Write a method anagram(s,t) to decide if two strings are anagrams or not.
'''

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        newS = ''.join(sorted(s))
        newT = ''.join(sorted(t))
        if newS == newT:
            return True
        else:
            return False

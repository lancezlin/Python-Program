'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        words = s.rstrip().lstrip().split()
        reWords = words[::-1]
        string = ' '.join(reWords)
        return string

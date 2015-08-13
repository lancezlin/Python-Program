'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Example
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        lft = '([{'
        rgt = ')]}'
        AS = []
        for item in s:
            if item in lft:
                AS.append(item)
            else:
                if item in rgt:
                    if len(AS) == 0:
                        return False
                    if rgt.index(item) != lft.index(AS.pop()):
                        return False
        return len(AS) == 0

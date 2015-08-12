'''
Given two binary strings, return their sum (also a binary string).

Example
a = 11
b = 1
Return 100
'''

class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        if a == '0' and b == '0':
            return '0'
        elif a == '0' and b != '0':
            return b
        elif a != '0' and b == '0':
            return a
        else:
            intA = int(a, 2)
            intB = int(b, 2)
            intAB = intA + intB
            return bin(intAB)[2:]

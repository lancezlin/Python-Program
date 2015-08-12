'''
Count how many 1 in binary representation of a 32-bit integer.

Example
Given 32, return 1

Given 5, return 2

Given 1023, return 9
'''

class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        binNum = bin(num)
        strBin = str(binNum)
        countOne = strBin.count('1')
        return countOne

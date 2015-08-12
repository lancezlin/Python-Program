'''
Reverse digits of an integer. Returns 0 when the reversed integer overflows (signed 32-bit integer).

Example
Given x = 123, return 321

Given x = -123, return -321
'''

class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here

            
        if n < 0:
            strN = str(-1 * n)
            reInt = -1 * int(strN[::-1])
            if reInt < -2**31:
                return 0
            else:
                return reInt
        elif n > 0:
            strN = str(n)
            reInt = int(strN[::-1])
            if reInt > 2**31-1:
                return 0
            else:
                return reInt
        return 0

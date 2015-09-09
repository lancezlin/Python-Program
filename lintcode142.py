'''
Using O(1) time to check whether an integer n is a power of 2.

Example:
For n=4, return true;

For n=5, return false;

Challenge
O(1) time
'''

class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            while n%2 == 0:
                n = n/2
                if n == 1:
                    return True
            return False

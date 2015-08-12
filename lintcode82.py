'''
Given 2*n + 1 numbers, every numbers occurs twice except one, find it.

Example
Given [1,2,2,1,3,4,3], return 4
'''

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        if len(A) == 0:
            return 0
        else:
            for i in A:
                if A.count(i) == 2:
                    pass
                else:
                    return i

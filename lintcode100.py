'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Example
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
'''

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        i = 0
        while i < len(A)-1:
            if A[i] == A[i+1]:
                A.remove(A[i])
                continue
            else:
                i += 1
        return len(A)

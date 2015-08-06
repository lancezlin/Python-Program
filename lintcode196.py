'''
Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.
Example:
Given N = 3 and the array [0, 1, 3], return 2.

'''
class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        '''
        missV = 0
        while missV < len(nums):
            nums.append(missV)
            if nums.count(missV) == 2:
                missV += 1
                nums.pop(-1)
            else:
                #missV += 1
                break
        return missV
        '''
        '''
        missV = None
        nums.sort()
        for i in xrange(0, len(nums)+1, 1):
            if nums.count(i) != 1:
                missV = i
        return missV
        '''
                missV = None
        i = 0
        while i <= len(nums):
            if i in nums:
                i += 1
            else:
                missV = i
                break
        return missV
        

'''
Given a unsorted array with integers, find the median of it. 

A median is the middle number of the array after it is sorted. 

If there are even numbers in the array, return the N/2-th number after sorted.

Example:
Given [4, 5, 1, 2, 3], return 3

Given [7, 9, 4, 5], return 5
'''

class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        nums.sort()
        start, stop = 0, len(nums)-1
        if len(nums) == 0:
            return 0
        elif len(nums) % 2 == 1:
            mid = nums[len(nums)//2]
        else:
            mid = nums[len(nums)/2-1]
        return mid

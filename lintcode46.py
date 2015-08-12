'''
Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.

Example
Given [1, 1, 1, 1, 2, 2, 2], return 1
'''

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        countDict = dict()
        for i in nums:
            if i not in countDict:
                countDict[i] = 1
            else:
                countDict[i] += 1
        maj = max(countDict.values())
        return countDict.keys()[countDict.values().index(maj)]

'''
Find the Nth number in Fibonacci sequence.

A Fibonacci sequence is defined as follow:

The first two numbers are 0 and 1.
The i th number is the sum of i-1 th number and i-2 th number.
The first ten numbers in Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

Example:
Given 1, return 0

Given 2, return 1

Given 10, return 34
'''

class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        preNum = 0
        curNum = 1
        endList = []
        if n <= 1:
            return 0
        else:
            while  len(endList) <= n-2:
                endNum = preNum + curNum
                preNum, curNum = curNum, endNum
                endList.append(preNum)
                continue
            return endList[-1]

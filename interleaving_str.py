# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:33:30 2015
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

@author: Lance
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i > 0 and dp[i-1][j] and s3[i+j-1] == s1[i-1]:
                    dp[i][j] = True
                elif j > 0 and dp[i][j-1] and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[len(s1)][len(s2)]
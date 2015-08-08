'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Example:
Given [1,2,3] which represents 123, return [1,2,4].

Given [9,9,9] which represents 999, return [1,0,0,0].

'''
class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        '''
        length = len(digits)
        digitNum = 0
        if length <= 1:
            digitNum = digits[0]
            pass
        else:
            for i in xrange(0, length-1, 1):
                digitNum += digits[i]*10**(digits[i])
        endNum = digitNum + 1
        nums = str(endNum)
        strNum = []
        for num in nums.split():
            strNum.append(num)
        strNum = [int(i) for i in strNum]
        return strNum
        '''
        length = len(digits)
        digitNum = 0
        '''
        if length <= 1:
            digitNum = digits[0]
            pass
        '''
        for i in xrange(0, length, 1):
            digitNum = digitNum + digits[i]*(10**(length-i-1))
        endNum = digitNum + 1
        listNum = [int(j) for j in str(endNum)]
        return listNum

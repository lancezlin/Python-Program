class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
        # Write your code here
        answer = 0
        if divisor == 1:
            answer = dividend
        elif divisor == -1:
            answer = 0 - dividend
        else:
            while dividend >= divisor:
                dividend = dividend - divisor
                answer += 1
        return answer

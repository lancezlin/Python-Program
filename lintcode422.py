'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

'''

class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        '''
        s = s.rstrip().lstrip().lower()
        # lens = len(s)
        countLW = 0
        lens = len(s)
        while lens > 0:
            if s[lens-1] != ' ':
                countLW += 1
                lens -= 1
                continue
            else:
                break
        return countLW
        '''
        s = s.rstrip().lstrip().lower()
        countLW = 0
        lastWord = []
        if len(s) > 1:
            for i in xrange(len(s)-1, 0, -1):
                while True:
                    if s[i] != ' ':
                        lastWord.append(s[i])
                        continue
                    else:
                        break
                countLW = len(lastWord)
        elif len(s) == 1:
            countLW = 1
        return countLW

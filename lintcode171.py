'''
Given an array of strings, return all groups of strings that are anagrams.

Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].
'''


'''
#Wrong solution
class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        i = 0
        output = list()
        while i <= len(strs)-1:
            j = 0
            while j<= len(strs)-1:
                if i == j:
                    pass
                else:
                    if len(strs[i])==0 and len(strs[j])==0:
                        output.append(strs[i])
                        output.append(strs[j])
                    else:
                        stri = ''.join(sorted(strs[i]))
                        strj = ''.join(sorted(strs[j]))
                        if stri == strj:
                            output.append(strs[i])
                            output.append(strs[j])
                j = j + 1
            i = i + 1
        outPut = []
        for k in xrange(0, len(output)-1):
            if k%2 == 0:
                outPut.append(output[k])
            else:
                pass
        return outPut
  '''

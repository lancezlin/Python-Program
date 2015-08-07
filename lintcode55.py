'''
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

Example:
For A = "ABCD", B = "ACD", return true.

For A = "ABCD", B = "AABC", return false.
'''
'''
class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        if B is None:
            return True
        else:
            listA = A.split()
            listB = B.split()
            i = 0
            while i < len(listB):
                if listA[i] not in listA:
                    return False
                    break
                else:
                    if listA.count(listB[i]) <= listB.count(listB[i]):
                        return False
                        break
                    else:
                        return True
                        continue
    '''
class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        listA = sorted(A)
        listB = sorted(B)
        for b in listB:
            if (b is not None) and ((b not in listA) or (listB.count(b) > listA.count(b))):
                return False
        return True

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

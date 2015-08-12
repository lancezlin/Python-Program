"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            for item in l2:
                l1.append(item)
            #while len(l2) > 0:
            #    l1.append(l2.pop())
        return l1.sort()

'''
Given a list, rotate the list to the right by k places, where k is non-negative.

Example:
Given 1->2->3->4->5 and k = 2, return 4->5->1->2->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        if head is None:
            return None
        elif k == 0 or k >= len(head):
            return head
        else:
            head1 = head[len(head)-k : len(head)]
            head2 = head[0 : len(head)-k]
            newHead = head2.append(head1)
            return newHead

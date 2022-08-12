"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
and return the new head.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = None
        cur = head
        h = head
        while cur:
            if cur.val == val:
                if pre:  # is not head
                    pre.next = cur.next
                    cur = cur.next
                else:  # is head
                    cur = cur.next
                    h = cur
            else:
                pre = cur
                cur = cur.next
        return h

"""
Runtime: 86 ms, faster than 54.74% of Python online submissions for Remove Linked List Elements.
Memory Usage: 20.4 MB, less than 27.53% of Python online submissions for Remove Linked List Elements.
"""
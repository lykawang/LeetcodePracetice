"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head:
            if head.next:  # at least 2 elements
                cur = head
                nex = cur.next
                cur.next = None

                while nex.next:
                    pre = cur
                    cur = nex
                    nex = nex.next
                    cur.next = pre

                pre = cur
                cur = nex
                cur.next = pre
                return cur
            else:  # only one element
                return head
        else:  # no element
            return head


"""
Runtime: 33 ms, faster than 61.27% of Python online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 53.31% of Python online submissions for Reverse Linked List.
"""

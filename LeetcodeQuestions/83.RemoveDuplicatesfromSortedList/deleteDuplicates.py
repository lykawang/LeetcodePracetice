"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the
linked list sorted as well.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:  # while cur is not None
            if cur.next and cur.val == cur.next.val:  # cannot work without "cur.next and"
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


'''
Runtime: 32 ms, faster than 81.40% of Python online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.4 MB, less than 86.80% of Python online submissions for Remove Duplicates from Sorted List.
'''

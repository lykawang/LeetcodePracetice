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

        node_next = head.next
        head.next = None
        self.connectToFront(node_next, head)

    def connectToFront(self, cur_node, pre_node):
        if cur_node.next == None:
            cur_node.next = pre_node
        else:
            node_next = cur_node.next
            cur_node.next = pre_node
            self.connectToFront(node_next, cur_node)

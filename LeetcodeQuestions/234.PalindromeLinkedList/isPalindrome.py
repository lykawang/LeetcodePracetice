"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    list_node = []
    cur_node = head
    while cur_node:
        list_node.append(cur_node.val)
        cur_node = cur_node.next
    i = 0 # the first index
    j = len(list_node) - 1 # the last index
    while i <= j:
        if list_node[i] == list_node[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

"""
runtime beats 12.69%, memory usage beats 40.97%
"""

    # one faster approach
    # l = []
    # while head:
    #     l.append(head.val)
    #     head = head.next
    # return l == l[::-1]  # directly check the list with its inverse
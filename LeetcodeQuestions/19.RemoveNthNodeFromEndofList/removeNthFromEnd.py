"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    cur = head
    count = 1
    pre = head
    while cur.next:
        pre = cur
        count += 1
        cur = cur.next
    if n == 1:
        if count == 1:
            return None
        else:
            pre.next = None
            return head
    elif n == count:
        head = head.next
        return head
    else:
        n_start = count - n + 1
        cur = head
        while n_start > 1:
            pre = cur
            cur = cur.next
            n_start -= 1
        pre.next = cur.next
        return head

"""
runtime beats 23.38%
memory usage beats 40.6%
"""





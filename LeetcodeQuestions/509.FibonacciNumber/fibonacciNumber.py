'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
the sum of the two preceding ones, starting from 0 and 1.

Given n, calculate F(n).
'''


def fib(n):
    """
    :type n: int
    :rtype: int
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    while n > 1:
        temp = b
        b = a + b
        a = temp
        n -= 1
    return b


print(fib(4))


# Runtime: 20 ms, faster than 79.99% of Python online submissions for Fibonacci Number.

# Memory Usage: 13.4 MB, less than 62.49% of Python online submissions for Fibonacci Number.
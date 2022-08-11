"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    else:
        a = 1
        b = 1
        while n - 2 > 0:
            temp = a
            a += b
            b = temp
            n -= 1
        return a + b


"""
Runtime: 24 ms, faster than 57.45% of Python online submissions for Climbing Stairs.
Memory Usage: 13.3 MB, less than 62.91% of Python online submissions for Climbing Stairs.
"""

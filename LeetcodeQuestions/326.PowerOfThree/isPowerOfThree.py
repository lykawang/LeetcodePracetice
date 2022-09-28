def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    while n % 3 == 0:
        n = n/3
    if n == 1:
        return True
    else:
        return False

"""
Runtime: 193 ms, faster than 13.14% of Python online submissions for Power of Three.
Memory Usage: 13.5 MB, less than 38.00% of Python online submissions for Power of Three.
"""
"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""


class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if (low % 2 == 0) and (high % 2 == 0):
            return (high - low) / 2
        else:
            return (high - low) / 2 + 1

"""
Runtime: 34 ms, faster than 17.41% of Python online submissions for Count Odd Numbers in an Interval Range.
Memory Usage: 13.5 MB, less than 34.14% of Python online submissions for Count Odd Numbers in an Interval Range.
"""

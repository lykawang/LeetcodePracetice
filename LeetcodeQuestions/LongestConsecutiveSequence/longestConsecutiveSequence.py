'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
'''


def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    i = 0
    n = 1
    max_n = 1
    if len(nums) == 0:
        return 0
    while i < len(nums) - 1:  # not the last one
        if nums[i] == nums[i + 1]:
            nums.pop(i + 1)
        elif nums[i] + 1 == nums[i + 1]:
            n += 1
            i += 1
        else:
            if max_n < n:
                max_n = n
            n = 1
            i += 1
    return max(max_n, n)


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums))

'''
Runtime: 370 ms, faster than 73.71% of Python online submissions for Longest Consecutive Sequence.
Memory Usage: 23.6 MB, less than 91.93% of Python online submissions for Longest Consecutive Sequence.
'''

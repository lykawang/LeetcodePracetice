'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    while len(nums) != 1:
        if nums[0] == nums[1]:
            nums.pop(0)
            nums.pop(0)
        else:
            return nums[0]
    return nums[0]

# runtime beats 29.44%
# memory usage beats 98.41%




def singleNumber(self, nums: List[int]) -> int:
    nums.sort()
    i = 0
    while i < len(nums):
        if i == len(nums) - 1:
            return nums[i]
        elif nums[i] != nums[i + 1]:
            return nums[i]
        i = i + 2
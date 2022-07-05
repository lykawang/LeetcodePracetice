'''
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.
'''


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    i = 0
    n = len(nums)
    while i < n-1:
        if nums[i] < nums[i+1]:
            i += 1
        else:
            return True
    return False

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))

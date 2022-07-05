'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    d = 0
    n = len(nums)
    while i+d < n:
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.append(0)
            d += 1
        else:
            i += 1


nums = [0,0,0,0,0,0,1,1,1]
moveZeroes(nums)
for i in nums:
    print(i)


'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        t = 1

        while i < len(nums):
            if nums[i] + nums[t] == target:
                return list((i, t))
            else:
                if t < len(nums) - 1:
                    t += 1
                else:
                    i += 1
                    t = i + 1
        '''
        Less memory storage way:
        n = len(nums)
        for i in range(0, n-1):
            diff = target - nums[i]
            for j in range(i+1, n):
                if nums[j] == diff:
                    return [i, j]
        '''

'''
Notes:
1. range() function
- range(a) 
  where 'a' is a number
  equals to [0,a)
- range(start, stop, step)
  equals to [start,stop)
  if step = 1, it can be ignored
'''






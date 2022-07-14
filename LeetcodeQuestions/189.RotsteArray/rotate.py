def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    temp_end = nums[0: n - k]
    temp_front = nums[n-k: n]
    nums[:] = temp_front + temp_end # can not directly use nums or nums[]

    # don't know why the below method is not accepted...
    # nums.clear()
    # nums.extend(temp_front)
    # nums.extend(temp_end)

nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
for x in nums:
    print(x)


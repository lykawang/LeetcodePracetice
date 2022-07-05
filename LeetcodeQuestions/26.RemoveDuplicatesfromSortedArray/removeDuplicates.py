'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the
first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # # Attempt 1  wrong method
    # i = 0
    # t = 0
    # d = 0
    # n = len(nums)
    # for t in range(n-1):
    #     if nums[i] != nums[i+1]:
    #         i += 1
    #         t += 1
    #     else:
    #         nums.remove(nums[i+1])
    #         d += 1
    #         nums.append(' ')
    #         t += 1
    #
    # return n-d
    # # Attempt 2  wrong method
    # i = 0
    # d = 0
    # n = len(nums)
    # while i < n-d-1:
    #     if nums[i] != nums[i+1]:
    #         i += 1
    #     else:
    #         nums.remove(nums[i+1])
    #         d += 1
    #         nums.append(' ')
    # return n-d


    # Attempt 3  runtime beats 58.26%, memory usage beats 78.28%
    i = 1
    o = 1
    n = len(nums)
    l = nums[n - 1]
    while i < n:
        if nums[i] != nums[i-1]:
            nums[o] = nums[i]
            i += 1
            o += 1
        elif nums[i] == l:
            break
        else:
            d = i-o+1
            while nums[i+1] == nums[i]:
                d += 1
                i += 1
            nums[o] = nums[i+1]
            i = o + d + 1
            o += 1
    return o



nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
for i in nums:
    print(i)

nums = [1,1,2,3]
print(removeDuplicates(nums))
for i in nums:
    print(i)


'''
Notes:
Some remove list item functions
1. remove() function
   list_name.remove( )
   inside the () is the specified item
   e.g.  thislist = ["apple", "banana", "cherry"]
         thislist.remove("banana")
         
2. pop() function
   list_name.pop( )
   inside the () is the specified index
   if no index specify, then remove the last one
   e.g.  thislist = ["apple", "banana", "cherry"]
         thislist.pop(1)
         
3. del keyword
   del list_name[ ]
   inside the [] is the specified index 
   e.g. thislist = ["apple", "banana", "cherry"]
        del thislist[0]
   
'''

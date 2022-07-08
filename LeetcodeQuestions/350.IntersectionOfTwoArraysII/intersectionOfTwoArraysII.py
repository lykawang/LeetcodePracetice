'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear
as many times as it shows in both arrays and you may return the result in any order.
'''


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1.sort()
    nums2.sort()
    x = 0
    while x < len(nums1) and x < len(nums2):
        if nums1[x] < nums2[x]:
            nums1.pop(x)
        elif nums1[x] > nums2[x]:
            nums2.pop(x)
        else:
            x += 1
    if x == len(nums1):
        return nums1
    else:
        return nums2


nums1 = [1,2]
nums2 = [1,1]
for x in intersect(nums1,nums2):
    print(x)


# runtime beats 34.39%

# memory usage beats 95.45%
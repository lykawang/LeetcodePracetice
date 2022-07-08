def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    max_out = []
    i1 = 0
    while i1 < len(nums1):
        c  = nums2.count(nums1[i1])
        while c != 0:
            out = []
            i2 = [t for t, x in enumerate(nums2) if x == nums1[i1]][c-1]
            out.append(nums2[i2])
            s = 1
            while i2+s < len(nums2) and i1+s < len(nums1):
                if i2 == len(nums2) - 1: # the last one
                    if len(out) > len(max_out):
                        max_out == out


# not finish but have thoughts

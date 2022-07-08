def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    # transform three strings into lists
    list_s1 = []
    for x in s1:
        list_s1.append(x)
    list_s2 = []
    for x in s2:
        list_s2.append(x)
    list_s3 = []
    for x in s3:
        list_s3.append(x)

    if len(list_s3) != len(list_s1) + len(list_s2):
        return False
    if len(list_s1) == 0:
        return list_s3 == list_s2
    if len(list_s2) == 0:
        return list_s3 == list_s1

    return helper(list_s1, list_s2, list_s3)


def helper(list_s1, list_s2, list_s3):
    while len(list_s3) > 0:
        if list_s1[0] != list_s2[0]:
            if list_s1[0] == list_s3[0]:
                list_s1.pop(0)
                list_s3.pop(0)
            elif list_s2[0] == list_s3[0]:
                list_s2.pop(0)
                list_s3.pop(0)
            else:
                return False
                break
        else:
            return helper(list_s1.pop(0), list_s2, list_s3.pop(0)) or helper(list_s1, list_s2.pop(0), list_s3.pop(0))



str1 = "aabcc"
str2 = "dbbca"
str3 = "aadbbcbcac"
isInterleave(str1,str2,str3)

# str1 = "a"
# str2 = ""
# str3 = "c"
# print(isInterleave(str1, str2, str3))

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle in haystack:
        if needle == '':
            return 0
        else:
            i = 0
            while i <= len(haystack) - len(needle):
                if haystack[i] == needle[0]:
                    if haystack[i:i+len(needle)] == needle:
                        return i
                    else:
                        i += 1
                else:
                    i += 1
    else:
        return -1

haystack = "aaaaa"
needle = "bba"
print(strStr(haystack, needle))

# runtime beats 89.95%

# memory usage beats 83.01%
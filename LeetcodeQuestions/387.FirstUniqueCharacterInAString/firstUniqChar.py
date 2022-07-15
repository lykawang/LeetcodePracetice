def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    dup = []
    index = 0
    while len(s) > 0:
        if len(s) == 1 and s[0] not in dup:
            return index
        elif s[0] not in s[1:] and s[0] not in dup:
            return index
        else:
            dup.append(s[0])
            index += 1
            s = s[1:]

    return -1

s = "aabb"
print(firstUniqChar(s))


# runtime beats 7.93%

# memory usage beats 50.09%

'''
Notes:
1. no pop() in string related methods
2. append()
   add an element at the end of the string, inside () is the content
3. find()
   searches the string for a specified value and returns the position of where it was found
'''
def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    n = len(s)
    t = 0
    while t < n // 2:
        s[t], s[n - 1 - t] = s[n - 1 - t], s[t]
        t += 1

    # shortcut:
    # 1. s[:]=s[::-1]
    #    list[< start >: < stop >: < step >]
    # 2. s.reverse()


s = ["h", "e", "l", "l", "o"]
reverseString(s)
for x in s:
    print(x)

# runtime beats 28.82%

# memory usage beats 77.73%

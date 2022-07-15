def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_list = []
    t_list = []
    for i in s:
        s_list.append(i)
    for p in t:
        t_list.append(p)
    s_list.sort()
    t_list.sort()
    return s_list == t_list



s = "rat"
t = 'car'
print(isAnagram(s,t))

# Notes
# String cannot use sort() directly

# runtime beats 11.24%
#memory usage beats 28.54%
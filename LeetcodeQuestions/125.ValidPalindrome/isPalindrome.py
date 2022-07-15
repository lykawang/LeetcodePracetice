def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s_all_letter = []
    for i in s.lower():
        if i.isalpha() or i.isdigit():
            s_all_letter.append(i)
    return s_all_letter == s_all_letter[::-1]


'''
Notes:
For string
.isalpha()  return true is the element is a letter
.isdigit()  return true is the element is a number
'''


s = "0P"
print(isPalindrome(s))

# runtime beats 91.87%

# memory usage beats 19.96%

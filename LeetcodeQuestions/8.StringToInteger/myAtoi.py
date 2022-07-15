def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    out = ''
    for i in s.strip(): # return removes any whitespace from the beginning or the end but not change itself
        if i == '-' or i == '+':
            if len(out) != 0:
                break
            else:
                out = out + i
        elif i.isdigit():
            out = out + i
        else:
            break
    if out == '' or out == '+' or out == '-':
        return 0
    elif int(out) > (2**31)-1:
        return (2**31)-1
    elif int(out) < -1*(2**31):
        return -1*(2**31)
    else:
        return int(out)



s = '-91283472332'
print(myAtoi(s))

# Runtime: 27 ms, faster than 78.59% of Python online submissions for String to Integer (atoi).

# Memory Usage: 13.6 MB, less than 49.24% of Python online submissions for String to Integer (atoi).



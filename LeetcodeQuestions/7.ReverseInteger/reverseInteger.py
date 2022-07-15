def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x >= (2**31)-1 or x <= -1*(2**31):
        return 0

    elif x >= 0:
        str_x = str(x)
        str_x = str_x[::-1]
        if int(str_x) >= (2 ** 31) - 1 or int(str_x) <= -1 * (2 ** 31):
            return 0
        else:
            return int(str_x)

    else:
        abs_x = abs(x)
        str_abs_x = str(abs_x)
        str_abs_x = str_abs_x[::-1]
        if -1*int(str_abs_x) >= (2 ** 31) - 1 or -1*int(str_abs_x) <= -1 * (2 ** 31):
            return 0
        else:
            return -1 * int(str_abs_x)

print(reverse(1534236469))


'''
Notes:
Reverse a string
str_a[::-1]
'''

# runtime beats 80.68%

# memory usage beats 37.42%
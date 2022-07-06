'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of
the integer. The digits are ordered from most significant to least significant in left-to-right order. The large
integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits.reverse()
    i = 0
    sum = 0
    while i < len(digits):
        sum += 10**i * digits[i]
        i += 1
    sum += 1
    sum_str = str(sum)
    output = []
    i = 0
    while i < len(sum_str):
        x = int(sum_str[i])
        i += 1
        output.append(x)
    return output


digits = [1,2,3]
for x in plusOne(digits):
    print(x)
"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming
weight).
"""


def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """

    str_n = str(bin(n))
    i = 0
    num = 0
    while i < len(str_n):
        if str_n[i:i + 1] == '1':
            num += 1
        i += 1
    return num
    """
    runtime beats 11.58%, memory usage beats 35.93%
    """

    # return bin(n).count('1')
    """
    runtime beats 98.93%
    """


n = 0b00000000000000000000000000001011
print(hammingWeight(n))

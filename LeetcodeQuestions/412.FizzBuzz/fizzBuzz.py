"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    output = []
    i = 1
    while i <= n:
        if i % 3 == 0:
            if i % 5 == 0:
                output.append("FizzBuzz")
            else:
                output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
        i += 1
    return output

#test case
print(fizzBuzz(15))

"""
runtime beats 48.2%, memory usage beats 95.56%
"""



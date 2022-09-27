"""
Given an integer n, return the number of prime numbers that are strictly less than n.
"""


def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """

    # Time Limit Exceeded
    # if n == 0 or n == 1:
    #     return 0
    # else:
    #     count = 0
    #     i = 2
    #     while i < n:
    #         j = 1
    #         check_times = 0
    #         while j <= i:
    #             if i % j == 0:
    #                 check_times += 1
    #             j += 1
    #         if check_times == 2:
    #             count += 1
    #         i += 1
    #     return count

    # Time Limit Exceeded
    # if n == 0 or n == 1 or n == 2:
    #     return 0
    # elif n == 3:
    #     return 1
    # elif n == 4 or n == 5:
    #     return 2
    # elif n == 6:
    #     return 3
    # else:
    #     count = 3
    #     prime_num = [2,3,5]
    #     i = 7
    #     while i < n:
    #         is_prime = True
    #         for x in prime_num:
    #             if x >= i/2:
    #                 break
    #             if i % x == 0:
    #                 is_prime = False
    #                 break
    #         if is_prime:
    #             count += 1
    #             prime_num.append(i)
    #         i += 2
    #     return count

    # other's solution
    # Time Limit Exceeded   # Last executed input:348436
    # if n <= 2:
    #     return 0
    # primes = [True] * n
    # primes[0] = primes[1] = False
    # for number in range(2, n): # for all elements in the range [2 , n)
    #     if primes[number]: # if it is a prime
    #         for multiple in range(2 * number, n, number):
    #             primes[multiple] = False
    # return sum(primes)

    # other's solution
    # Time Limit Exceeded for the first time   # Last executed input: 993422
    # second time pass
    nums = [0, 0] + [1] * (n - 2)
    for i in range(2, int(sqrt(n) + 1)):
        if nums[i] == 1:
            for j in range(i * i, n, i):
                nums[j] = 0
    return sum(nums)


print(countPrimes(50000))

# Implement a function, find_missing_number() that returns the missing number in a sorted array of sequential integers.
# Starts at 0. There is always one and only one missing element.

def find_missing_number(sort_list):
    expect_num = 0
    for i in sort_list:
        if i == expect_num:
            expect_num += 1
        else:
            return expect_num
    return expect_num



assert (find_missing_number([0, 1, 2, 3, 4, 5, 7]) == 6)
assert (find_missing_number([1, 2, 3, 4, 5, 6, 7]) == 0)
assert (find_missing_number([0, 1, 2, 3, 4, 5, 6]) == 7)

from random import randint

randnum = randint(0, 1000)
test_list = list(range(0, 1001))
test_list.pop(randnum)
assert (find_missing_number(test_list) == randnum)
test_list = list(range(0, 1001))
test_list = test_list[:-1]
assert (find_missing_number(test_list) == 1000)
print("Passed.")
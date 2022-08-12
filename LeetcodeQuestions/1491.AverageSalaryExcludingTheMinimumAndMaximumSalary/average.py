"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual
answer will be accepted.
"""


def average(salary):
    """
    :type salary: List[int]
    :rtype: float
    """
    # my edition
    salary.sort()
    sum = 0
    for i in range(1, len(salary)-1):
        sum += salary[i]
    return sum*1.00000/(len(salary)-2)

    # short edition
    # return (sum(salary) - max(salary) - min(salary)) / float(len(salary)-2)


salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
print(average(salary))


"""
Runtime: 24 ms, faster than 66.26% of Python online submissions for Average Salary Excluding the Minimum and Maximum Salary.
Memory Usage: 13.5 MB, less than 47.33% of Python online submissions for Average Salary Excluding the Minimum and Maximum Salary.

For the short edition:
Runtime: 19 ms, faster than 85.63% of Python online submissions for Average Salary Excluding the Minimum and Maximum Salary.
"""
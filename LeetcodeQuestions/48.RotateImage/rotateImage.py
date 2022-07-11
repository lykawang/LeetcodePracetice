'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
another 2D matrix and do the rotation.

'''


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    temp = []
    x = len(matrix) - 1
    while n >= 0:
        temp += matrix[x]
        x -= 1
    i = 0
    j = 0
    t = 0
    while i < len(matrix):
        while j < len(matrix):
            matrix[i][j] = temp[t]
            t += 1
            j += 1
        i += 1
        j = 0


    # BETTER WAY
    # N = len(matrix)
    # for r in range(N):
    #     for c in range(r):
    #         matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c] # when swapping, no necessary to write temp
    # for r in matrix:
    #     r.reverse()


# runtime beats 90.20%
# memory usage beats 90.28%

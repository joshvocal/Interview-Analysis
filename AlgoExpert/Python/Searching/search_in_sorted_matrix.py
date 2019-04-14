'''
Solution 1:
Time: O(logn + logm)
Space: O(1)
'''


def searchInSortedMatrix(matrix, target):
    if not matrix or not len(matrix) or not len(matrix[0]):
        return [-1, -1]

    rows = len(matrix)
    cols = len(matrix[0])

    row = rows
    col = 0

    while col <= cols and row >= 0:
        if matrix[row][col] == target:
            return [row, col]
        elif matrix[row][col] > target:
            row -= 1
        else:
            col += 1

    return [-1, -1]



"""
Solution 1: Brute Force
Time: O(n*m)
Space: O(1)
"""

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == target:
                    return True

        return False


"""
Solution 2: Modified Search
Time: O(m+n)
Space: O(1)
"""

class Solution2:
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and 0 <= col:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True

        return False
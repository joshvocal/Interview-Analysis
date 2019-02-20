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



"""
Solution 3: Row Binary Search
Time: O(n*log(m))
Space: O(1)
"""

class Solution3:
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        lo = 0
        hi = len(matrix[0]) - 1
        
        for row in matrix:
            print(row)
            if target <= row[hi]:
                while lo <= hi:
                    mid = (lo + hi) // 2
                    
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        hi = mid - 1
                    else:    
                        lo = mid + 1
                lo = 0       
                hi = len(row) - 1

        return False
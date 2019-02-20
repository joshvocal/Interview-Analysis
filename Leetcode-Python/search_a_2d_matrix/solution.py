"""
Solution 1: Brute Force
Time: O(n*m)
Space: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == target:
                    return True
                
        return False
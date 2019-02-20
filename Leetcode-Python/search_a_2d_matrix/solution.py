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


"""
Solution 2: Row Binary Search
Time: O(n*log m)
Space: O(1)
"""

class Solution2:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        for row in matrix:
            if target <= row[len(row) - 1]:
                return self.binary_search(row, target, 0, len(row) - 1)
        
        return False
    
    def binary_search(self, nums, target, lo, hi):
        if hi < lo:
            return False
            
        mid = (lo + hi) // 2
            
        if target == nums[mid]:
            return True
        elif target < nums[mid]:
            return self.binary_search(nums, target, lo, mid - 1)
        else:
            return self.binary_search(nums, target, mid + 1, hi)
        
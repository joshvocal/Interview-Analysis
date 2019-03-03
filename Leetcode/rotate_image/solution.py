class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row = len(matrix)
        col = len(matrix[0])
        
        for i in range(row):
            for j in range(i, col):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        for i in range(row):
            for j in range(col // 2):
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][col - j - 1]
                matrix[i][col - j - 1] = temp
                
"""
Solution 1: DFS
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        matrix = grid
        biggest = 0

        if not matrix or not len(matrix) or not len(matrix[0]):
            return 0

        height = len(matrix)
        width = len(matrix[0])

        for x in range(height):
            for y in range(width):
                if matrix[x][y] == 1:
                    biggest = max(biggest, self.dfs(
                        matrix, x, y, height, width, 0))

        return biggest

    def dfs(self, matrix, x, y, height, width, counter):
        if x < 0 or y < 0 or x >= height or y >= width or matrix[x][y] == 0:
            return 0

        matrix[x][y] = 0

        right = self.dfs(matrix, x + 1, y, height, width, counter + 1)
        down = self.dfs(matrix, x, y - 1, height, width, counter + 1)
        left = self.dfs(matrix, x - 1, y, height, width, counter + 1)
        up = self.dfs(matrix, x, y + 1, height, width, counter + 1)

        return left + right + up + down + 1

"""
Solution 1: DFS
Time: O()
Space: O()
"""


class Solution:
    def numIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        numRows = len(grid)
        numCols = len(grid[0])
        numIslands = 0

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == '1':
                    self.dfs(grid,i ,j, numRows, numCols)
                    numIslands += 1

        return numIslands

    def dfs(self, grid, i, j, numRows, numCols):
        if i < 0 or j < 0 or numRows <= i or numCols <= j or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j, numRows, numCols)
        self.dfs(grid, i - 1, j, numRows, numCols)
        self.dfs(grid, i, j + 1, numRows, numCols)
        self.dfs(grid, i, j - 1, numRows, numCols)


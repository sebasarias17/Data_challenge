class Solution:
    def getMaximumGold(self, grid):
        numRows, numCols = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= numRows or col >= numCols or grid[row][col] == 0:
                return 0

            original_value = grid[row][col]
            grid[row][col] = 0

            maxGold = 0
            for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                maxGold = max(maxGold, dfs(r, c))

            grid[row][col] = original_value

            return maxGold + original_value

        maxGold = 0
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] != 0:
                    maxGold = max(maxGold, dfs(row, col))

        return maxGold
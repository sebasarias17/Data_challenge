class Solution:
    def getMaximumGold(self, grid):
        numRows, numCols = len(grid), len(grid[0])

        def dfs(row, col, visited):

            if row < 0 or col < 0:
                return 0
            if row >= numRows or col >= numCols:
                return 0

            if grid[row][col] == 0:
                return 0

            if (row, col) in visited:
                return 0

            visited.add((row, col))
            gold = grid[row][col]
            direction_moves = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for nextRow, nextCol in direction_moves:
                gold = max(gold, grid[row][col] + dfs(nextRow, nextCol, visited))
            visited.remove((row, col))
            return gold

        maxGold = 0
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] != 0:
                    maxGold = max(maxGold, dfs(row, col, set()))
        return maxGold

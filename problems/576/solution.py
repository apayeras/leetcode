"""
576. Out of Boundary Paths
"""
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        cache = {}
        def calculatePaths(row, col, remainingMove):
            if  (0 > row or row == m) or (0 > col or col == n):
                return 1
            if remainingMove == 0:
                return 0
            if (row, col, remainingMove) in cache:
                return cache[(row, col, remainingMove)]

            cache[(row, col, remainingMove)] = (
                (calculatePaths(row + 1, col, remainingMove - 1) + 
                calculatePaths(row - 1, col, remainingMove - 1)) % MOD + 
                (calculatePaths(row, col + 1, remainingMove - 1) + 
                calculatePaths(row, col - 1, remainingMove - 1)) % MOD
            ) % MOD
            return cache[(row, col, remainingMove)]
        return calculatePaths(startRow, startColumn, maxMove)

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.findPaths(8, 7, 16, 1, 6))
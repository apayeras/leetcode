"""
931. Minimum Falling Path Sum
"""
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        cache = {}
        def fallingPath(row, col):
            if (row, col) in cache:
                return cache[(row, col)]
            nodeVal = matrix[row][col]
            if row == len(matrix) - 1:
                return nodeVal
            if col >= len(matrix) - 1:
                res = nodeVal + min(fallingPath(row + 1, col), fallingPath(row + 1, col - 1))
            elif col <= 0:
                res = nodeVal + min(fallingPath(row + 1, col), fallingPath(row + 1, col + 1))
            else:
                res = nodeVal + min(fallingPath(row + 1, col), fallingPath(row + 1, col + 1), fallingPath(row + 1, col - 1))
            cache[(row, col)] = res
            return res


        sol =  float('inf')
        for i in range(len(matrix)):
            sol = min(sol, fallingPath(0, i))
        return sol

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
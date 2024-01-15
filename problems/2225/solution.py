"""
1704. Determine if String Halves Are Alike
"""

from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        print()

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
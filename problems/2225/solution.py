"""
1704. Determine if String Halves Are Alike
"""

from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        games = {}
        lose0, lose1 = [], []
        for match in matches:
            if match[0] not in games:
                games[match[0]] = 0
            if match[1] not in games:
                games[match[1]] = 1
            else:
                games[match[1]] += 1
        for elems in games.items():
            if elems[1] == 0:
                lose0.append(elems[0])
            elif elems[1] == 1:
                lose1.append(elems[0])
        return [sorted(lose0), sorted(lose1)]

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
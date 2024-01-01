"""
455. Assign Cookies
"""
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        childs = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                childs += 1
                i += 1
            j += 1
        return childs

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.findContentChildren([3,2,1], [1,1]))
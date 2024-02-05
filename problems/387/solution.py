"""
387. First Unique Character in a String
"""
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        values = Counter(s)
        for idx, char in enumerate(s):
            if values[char] == 1:
                return idx
        return -1
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))
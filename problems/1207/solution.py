"""
1207. Unique Number of Occurrences
"""
from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        repeated = Counter(arr)
        return len(repeated) == len(set(repeated.values()))

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
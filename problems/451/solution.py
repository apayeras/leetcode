"""
451. Sort Characters By Frequency
"""
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        return "".join(x[0]*x[1] for x in (sorted(count.items(), key = lambda x: x[1], reverse = True)))
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.frequencySort("tree"))
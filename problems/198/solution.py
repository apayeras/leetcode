"""
198. House Robber
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def aux(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            res = max(nums[i] + aux(i+2), aux(i+1))
            cache[i] = res
            return res
        return aux(0)
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1,2,3,1]))
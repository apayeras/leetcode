"""
268. Missing Number
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pairs = set(x for x in range(len(nums)+1))
        for num in nums:
            pairs.remove(num)
        return list(pairs)[0]
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([3,0,1]))
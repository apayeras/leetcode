"""
645. Set Mismatch
"""
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeated = set(i for i in range(1, len(nums) + 1))
        sol = []
        for i in range(len(nums)):
            if nums[i] in repeated:
                repeated.remove(nums[i])
            else:
                sol.append(nums[i])

        return sol + list(repeated)
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.findErrorNums([1,2,2,4]))
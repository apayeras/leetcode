"""
2966. Divide Array Into Arrays With Max Difference
"""
from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        size = len(nums)
        if size % 3 != 0:
            return []

        nums.sort()

        result = []
        group_index = 0
        for i in range(0, size, 3):
            if i + 2 < size and nums[i + 2] - nums[i] <= k:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
                group_index += 1
            else:
                return []
        return result
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.divideArray([1,3,4,8,7,9,3,5,1], 2))
"""
2870. Minimum Number of Operations to Make Array Empty
"""
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        repeated = {}
        operations = 0
        for num in nums:
            if num in repeated:
                repeated[num] += 1
            else:
                repeated[num] = 1

        for val in repeated.values():
            if val == 1:
                return -1
            operations += val // 3
            if val % 3 != 0:
                operations += 1
        return operations
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations([2,3,3,2,2,4,2,3,4]))
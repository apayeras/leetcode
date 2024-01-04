"""
2870. Minimum Number of Operations to Make Array Empty
"""
from collections import Counter
import math
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        repeated = Counter(nums)
        operations = 0
        for val in repeated.values():
            if val == 1:
                return -1
            operations += math.ceil(val / 3)
        return operations
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations([2,3,3,2,2,4,2,3,4]))
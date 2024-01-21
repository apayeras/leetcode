"""
907. Sum of Subarray Minimums
"""
from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        mod = 10**9 + 7
        arr = [float('-inf')] + arr + [float('-inf')]
        stack = []

        for idx, val in enumerate(arr):
            while stack and val < stack[-1][1]:
                j, el = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = idx - j
                res = (res + el * left * right) % mod

            stack.append((idx, val))

        return res
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.sumSubarrayMins([3,1,2,4]))
"""
1043. Partition Array for Maximum Sum
"""
from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        K = k + 1

        dp = [0] * K

        for start in range(N - 1, -1, -1):
            curr_max = 0
            end = min(N, start + k)

            for i in range(start, end):
                curr_max = max(curr_max, arr[i])
                dp[start % K] = max(dp[start % K], dp[(i + 1) % K] + curr_max * (i - start + 1))

        return dp[0]
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSumAfterPartitioning([1,15,7,9,2,5,10], 3))
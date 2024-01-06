"""
1235. Maximum Profit in Job Scheduling
"""
from typing import List
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
      
        number_of_jobs = len(profit)
      
        dp = [0] * (number_of_jobs + 1)
      
        for i, (current_end_time, current_start_time, current_profit) in enumerate(jobs):
            index = bisect_right(jobs, current_start_time, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[index] + current_profit)
      
        return dp[number_of_jobs]
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))
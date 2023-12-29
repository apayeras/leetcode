"""

"""
from collections import List
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        cache = {}

        def schedule(idx, columnValue, remainingDays):
            if (idx, columnValue, remainingDays) in cache:
                return cache[(idx, columnValue, remainingDays)]

            currentMax = max(columnValue, jobDifficulty[idx])
            if remainingDays == 1:
                res = max(max(jobDifficulty[idx:]), columnValue)
            elif remainingDays == len(jobDifficulty) - idx:
                res = sum(jobDifficulty[idx+1:]) + currentMax
            else:
                res = min(
                    schedule(idx + 1, currentMax, remainingDays),
                    currentMax + schedule(idx + 1, jobDifficulty[idx+1], remainingDays-1)
                )
            cache[(idx, columnValue, remainingDays)] = res
            return res

        return schedule(0, jobDifficulty[0], d)
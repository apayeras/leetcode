"""
2610. Convert an Array Into a 2D Array With Conditions
"""
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        rows = 1
        last = {}
        solution = [[]]
        for num in nums:
            if num in last:
                last[num] += 1
                if last[num] == rows: 
                    rows += 1
                    solution.append([num])
                else:
                    solution[last[num]].append(num)
            else:
                solution[0].append(num)
                last[num] = 0 
        return solution
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMatrix([1,3,4,1,2,3,1]))
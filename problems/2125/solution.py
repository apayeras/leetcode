"""
2125. Number of Laser Beams in a Bank
"""
from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        laserElements = 0
        for row in bank:
            securityDevices = row.count('1')
            beams += laserElements * securityDevices
            if securityDevices > 0:
                laserElements = securityDevices
        return beams
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfBeams(["011001","000000","010100","001000"]))
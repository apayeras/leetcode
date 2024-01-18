"""
70. Climbing Stairs
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prv1, prv2 = 1, 2
        res = 0
        for _ in range(2, n):
            res = prv1 + prv2
            prv1 = prv2
            prv2 = res
        return res
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(3))
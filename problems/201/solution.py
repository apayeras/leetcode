"""
201. Bitwise AND of Numbers Range
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.rangeBitwiseAnd(5, 7))
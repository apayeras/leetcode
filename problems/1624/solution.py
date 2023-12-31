"""
1624. Redistribute Characters to Make All Strings Equal
"""
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        high = -1
        first = [-1] * 26
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if first[idx] != -1:
                high = max(high, i - first[idx] - 1)
            else:
                first[idx] = i
        return high

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxLengthBetweenEqualCharacters("aa"))
"""
1704. Determine if String Halves Are Alike
"""
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        middle = len(s) // 2
        count = 0
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                if i < middle:
                    count += 1
                else:
                    count -= 1
        return count == 0

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.halvesAreAlike("book"))
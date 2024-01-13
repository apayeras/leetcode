"""
1347. Minimum Number of Steps to Make Two Strings Anagram
"""
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = [0] * 26
        sol = 0
        for letter in s:
            freq[ord(letter) - ord('a')] += 1
        for letter in t:
            i = ord(letter) - ord('a')
            if freq[i] > 0:
                freq[i] -= 1
            else:
                sol += 1
        return sol

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.minSteps("bab", "aba"))
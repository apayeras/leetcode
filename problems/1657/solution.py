"""
1704. Determine if String Halves Are Alike
"""
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        frequency_w1 = Counter(word1)
        frequency_w2 = Counter(word2)

        sorted_w1 = sorted(frequency_w1.values())
        sorted_w2 = sorted(frequency_w2.values())
      
        keys_match = set(frequency_w1.keys()) == set(frequency_w2.keys())

        return sorted_w1 == sorted_w2 and keys_match

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.closeStrings("cabbba", "abbccc"))
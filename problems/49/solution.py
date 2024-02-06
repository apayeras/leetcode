"""
49. Group Anagrams
"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            a = ''.join(sorted(s))
            if a in anagrams:
                anagrams[a].append(s)
            else:
                anagrams[a] = [s]
        return anagrams.values()
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
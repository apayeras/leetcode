"""
1897. Redistribute Characters to Make All Strings Equal
"""
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        alphabet = [0] * 26
        for word in words:
            for letter in word:
                alphabet[ord(letter) - ord('a')] += 1
        
        for repeated in alphabet:
            if repeated % n != 0:
                return False
        
        return True
    
## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.makeEqual(["abc","aabc","bc"]))
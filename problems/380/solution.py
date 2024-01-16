"""
300. Longest Increasing Subsequence
"""
from random import randrange

class RandomizedSet:
    def __init__(self):
        self.nums = {}
        self.ind = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        self.nums[val] = self.size
        self.ind[self.size] = val
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums:
            return False
        self.size -= 1
        idx = self.nums[val]
        last_val = self.ind[self.size]
        self.nums[last_val] = idx
        self.ind[idx] = last_val
        del self.nums[val]
        del self.ind[self.size]
        return True

    def getRandom(self) -> int:
        num = randrange(self.size)
        return self.ind[num]

## Check solution
if __name__ == "__main__":
    sol = RandomizedSet()
    print(sol.insert(2))
    print(sol.insert(4))
    print(sol.getRandom())
    print(sol.remove(2))
"""
232. Implement Queue using Stacks
"""
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1
    
## Check solution
if __name__ == "__main__":
    sol = MyQueue()
    print(sol.push(1))
    print(sol.push(2))
    print(sol.peek())
    print(sol.pop())
    print(sol.empty())
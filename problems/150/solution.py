"""
198. House Robber
"""
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    stack[-2] +=  stack[-1]
                    stack = stack[:-1]
                case '-':
                    stack[-2] -=  stack[-1]
                    stack = stack[:-1]
                case '*':
                    stack[-2] *=  stack[-1]
                    stack = stack[:-1]
                case '/':
                    stack[-2] =  int(stack[-2]/stack[-1])
                    stack = stack[:-1]
                case _:
                    stack.append(int(token))
        return stack[0]

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["2","1","+","3","*"]))
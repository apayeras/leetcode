"""
2385. Amount of Time for Binary Tree to Be Infected
"""
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        start_elem = None
        def dfs(node):
            if node == None:
                return
            if node.left != None:
                node.left.top = node
            if node.right != None:
                node.right.top = node
            if node.val == start:
                nonlocal start_elem
                start_elem = node
            dfs(node.left)
            dfs(node.right)
            
        root.top = None
        dfs(root)
        q = deque()
        q.append((0, start_elem))
        visited = set()
        sol = 0
        while len(q) > 0:
            idx, node = q.popleft()
            visited.add(node.val)
            for elem in [node.left, node.right, node.top]:
                if elem != None and elem.val not in visited:
                    q.append((idx + 1, elem))
                    sol = max(sol, idx + 1)
        return sol

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.amountOfTime([1,5,3,None,4,10,6,9,2], 3))
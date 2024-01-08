"""
938. Range Sum of BST
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def expandTree(node):
            if node == None:
                return 0
            if  low <= node.val <= high:
                return node.val + expandTree(node.left) + expandTree(node.right)
            elif node.val >= high:
                return expandTree(node.left)
            else:
                return expandTree(node.right)
        return expandTree(root)

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.rangeSumBST([10,5,15,3,7,None,18], 7, 15))
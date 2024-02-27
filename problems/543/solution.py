"""
543. Diameter of Binary Tree
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        def maxDiameter(node):
            if node.left == None and node.right == None:
                return 0
            left, right = 0, 0
            if node.left != None:
                left = 1 + maxDiameter(node.left)
            if node.right != None:
                right = 1 + maxDiameter(node.right)
            self.max = max(left + right, self.max)
            return max(left, right)
        maxDiameter(root)
        return self.max
"""
872. Leaf-Similar Trees
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findLeaf(node, sequence):
            if node == None:
                return sequence
            if node.left == None and node.right == None:
                sequence.append(node.val)
            sequence = findLeaf(node.left, sequence)
            sequence = findLeaf(node.right, sequence)
            return sequence
        return findLeaf(root1, []) == findLeaf(root2, [])

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.leafSimilar([3,5,1,6,2,9,8,None,None,7,4], [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]))
"""
1026. Maximum Difference Between Node and Ancestor
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        dif = 0
        def dif_ancestor(node, min_v, max_v):
            if node == None:
                return

            nonlocal dif
            dif = max(dif, max(abs(node.val - min_v), abs(max_v - node.val)))
            min_v = min(node.val, min_v)
            max_v = max(node.val, max_v)
            
            dif_ancestor(node.left, min_v, max_v)
            dif_ancestor(node.right, min_v, max_v)

        dif_ancestor(root, root.val, root.val)
        return dif

## Check solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAncestorDiff([8,3,10,1,6,None,14,None,None,4,7,13]))
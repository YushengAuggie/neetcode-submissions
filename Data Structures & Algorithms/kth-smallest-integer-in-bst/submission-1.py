# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        cns = k
        res = root.val

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res, cns
            if not node:
                return
            dfs(node.left)
            cns -= 1
            if cns == 0:
                res = node.val
                return res
            dfs(node.right)
            return res
        
        dfs(root)
        return res
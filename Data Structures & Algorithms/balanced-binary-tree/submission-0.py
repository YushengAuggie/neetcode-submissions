# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Time: O(n)
        Space: O(h)
        """
        
        def dfs(cur:Optional[TreeNode]) -> int:
            if not cur:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            if left == -1 or right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return dfs(root) != -1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_distance = 0

        def helper(node: Optional[TreeNode]) -> int:
            nonlocal max_distance
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right) 

            distance = left + right
            max_distance = max(max_distance, distance)

            return 1 + max(left, right)
        
        helper(root)
        return max_distance


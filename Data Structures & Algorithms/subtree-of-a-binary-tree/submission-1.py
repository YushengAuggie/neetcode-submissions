# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def same_tree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 or not node2:
            return node1 is None and node2 is None
        if node1.val == node2.val:
            left = self.same_tree(node1.left, node2.left)
            right = self.same_tree(node1.right, node2.right)
            return left and right
        return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
            
        if self.same_tree(root, subRoot):
            return True
        
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        return False
            
        
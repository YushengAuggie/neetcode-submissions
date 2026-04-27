# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        leverage the BST property / characristic 
        left < root < right
        so we just need to find the character that smaller<target<larger
        """
        if p.val < q.val:
            smaller = p
            larger = q
        else:
            smaller = q
            larger = p

        while root:
            if smaller.val <= root.val <= larger.val:
                return root

            if root.val < smaller.val:
                root = root.right
            else:
                root = root.left

        return root


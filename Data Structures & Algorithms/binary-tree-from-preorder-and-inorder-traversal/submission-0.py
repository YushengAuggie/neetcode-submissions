# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        pre-order: root, left{xxx}, right{xxx}

        in-order: left{xxx}, root, right{xxx}

        """
        # find the root: preorder[0]
        # left inorder[:inorder.find(root)] right inorder[inorder.find(root):]
        # keep doing it
        # time: n spce: O(n)
        if not preorder or not inorder:
            return None
        val = preorder[0]

        if len(preorder) == 1:
            return TreeNode(val)

        print(val)
        root = TreeNode(val)
        inorder_root_idx = inorder.index(val)
        left_inorder = inorder[:inorder_root_idx]
        right_inorder = inorder[inorder_root_idx + 1:]

        left_size = len(left_inorder)
        left_preorder = preorder[1:left_size + 1]
        right_preorder = preorder[left_size + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root


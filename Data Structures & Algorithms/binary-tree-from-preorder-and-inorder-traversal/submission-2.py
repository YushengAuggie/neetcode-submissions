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
        # time: O(n) space: O(n)

        inorder_index_map = {}
        for idx, val in enumerate(inorder):
            inorder_index_map[val] = idx
        
        # we know the first one of the pre-order is the next root
        root_idx = 0
        def dfs(left_bound:int, right_bound:int) -> Optional[TreeNode]:
            nonlocal root_idx
            if left_bound > right_bound:
                return None
            root_val = preorder[root_idx]
            root_idx += 1
            root = TreeNode(root_val)
            mid = inorder_index_map[root_val]
            left = dfs(left_bound, mid - 1)
            right = dfs(mid + 1, right_bound)
            root.left = left
            root.right = right
            return root

        return dfs(0, len(preorder) - 1)

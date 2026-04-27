# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        get the max sub-sequence
        # choose the next one or not - > next one and following is >0
        # either left, right, or non
        # res = max(0, res, max_of_cur)
        """
        def find_max(cur):
            nonlocal res
            if not cur:
                return 0
            left = max(find_max(cur.left), 0)
            right = max(find_max(cur.right), 0)
            cur_max = left + right + cur.val
            res = max(res, cur_max)
            return max(left, right) + cur.val

        res = float("-inf")
        find_max(root)
        return res
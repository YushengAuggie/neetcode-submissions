# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BST,
        time O(n) space O(n)
        """
        if not root:
            return []

        ret_list = []
        cur_level = deque()
        cur_level.append(root)
        while cur_level:
            next_level = deque()
            cur_level_vals = []
            while cur_level:
                cur = cur_level.popleft()
                cur_level_vals.append(cur.val)
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
            ret_list.append(cur_level_vals)
            cur_level = next_level
        return ret_list




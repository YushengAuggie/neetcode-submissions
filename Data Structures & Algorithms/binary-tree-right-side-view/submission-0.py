# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs, only last element every row
        # time: O(n), n is number of elements
        # spaceL O(n)
        if root is None:
            return []
        current_level = [root]
        res = []
        while current_level:
            next_level = []
            while current_level:
                cur = current_level.pop(0)
                if not current_level:
                    res.append(cur.val)
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
            current_level = next_level
        return res



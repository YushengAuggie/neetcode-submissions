# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        time: O(n) # number of nodes
        space: O(n) level of tree

        """

        def dfs(cur: TreeNode, cur_largest: int) -> int:
            if cur is None:
                return 0
            count = 0
            if cur.val >= cur_largest:
                count += 1
            cur_largest = max(cur_largest, cur.val)
            left_count = dfs(cur.left, cur_largest)
            right_count = dfs(cur.right, cur_largest)
            return count + left_count + right_count

        return dfs(root, root.val)

            
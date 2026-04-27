# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def withinBoundary(self, min_bound:int, max_bound:int, node:Optional[TreeNode]) -> bool:
        if node is None:
            return True

        print(f"{node.val=} {min_bound=} {max_bound=}")
        if node.val <= min_bound or node.val >= max_bound:
            return False

        # check decendents
        # print(f"left {node.left.val}")
        # print(f"right {node.right.val}")
        return self.withinBoundary(
            min_bound, node.val, node.left
        ) and self.withinBoundary(
            node.val, max_bound, node.right
        )




    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # binary tree
        # left < middle < right

        if not root:
            return True

        min_bound = float("-inf")
        max_bound = float("inf")
        # left < root < right
        # left decendents < root         
        # right decendents > root

        return self.withinBoundary(min_bound, max_bound, root)

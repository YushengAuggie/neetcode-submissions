# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        the smallest is always the left most
        and then root
        and then right
        # how many numbers are smaller than target 
        # k - 1 numbers should be smaller than this
        time O(n) space O(k)
        """
        def helper(node: Optional[TreeNode], k_list:list[int]) -> None:
            if node is None:
                return

            if len(k_list) == k:
                return

            helper(node.left, k_list)
            if len(k_list) < k:
                k_list.append(node.val)
            helper(node.right, k_list)
            return
        k_list = []
        helper(root, k_list)
        return k_list[-1]

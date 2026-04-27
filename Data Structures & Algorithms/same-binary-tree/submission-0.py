# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def cmp(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            if n1 is None or n2 is None:
                return n1 is None and n2 is None
            return n1.val == n2.val

        left_queue = [p]
        right_queue = [q]
        current_level = 2

        while left_queue and right_queue:
            next_level = 0
            while current_level:
                left = left_queue.pop()
                right = right_queue.pop()
                if not cmp(left, right):
                    return False
                else:
                    if left is not None:
                        left_queue.append(left.left)
                        left_queue.append(left.right)
                        next_level += 2
                    if right is not None:
                        right_queue.append(right.left)
                        right_queue.append(right.right)
                        next_level += 2
                current_level -= 2
            current_level = next_level
        return True
                    

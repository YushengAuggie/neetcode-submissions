# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findPath(self, root:TreeNode, target:TreeNode) -> list[TreeNode]:
        ret_list = []
        if root.val == target.val:
            return [target]
        else:
            if root.left:
                left_list = self.findPath(root.left, target)
                if left_list:
                    return [root] + left_list
            if root.right:
                right_list = self.findPath(root.right, target)
                if right_list:
                    return [root] + right_list
            return []
                    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Brute force
        find all the nodes from p to root,
        and find all the nodes from q to root,
        and find the first common one
        time: O(n) spce: O(1)
        """
        path_to_p = self.findPath(root, p)
        path_to_q = self.findPath(root, q)

        print([node.val for node in path_to_p])
        print([node.val for node in path_to_q])
        visited = set([node.val for node in path_to_p])
        print([val for val in visited])
        for node in path_to_q[::-1]:
            print(node.val)
            if node.val in visited:
                print("find")
                return node
        return None

        
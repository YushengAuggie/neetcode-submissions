# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def serilize(self, node: Optional[TreeNode]) -> list:
        if not node:
            return ["#"]
            
        ret_list = []
        ret_list.append(node.val)
        left = self.serilize(node.left)
        right = self.serilize(node.right)
        ret_list.extend(left)
        ret_list.extend(right)
        return ret_list

    def is_naive_subString(self, root_list: list[str], sub_root_list: list[str]) -> bool:
        # naive
        i = j = 0
        while i < len(root_list):
            prev = i
            while i < len(root_list) and root_list[i] == sub_root_list[j]:
                i += 1
                j += 1
                if j == len(sub_root_list):
                    return True
                    
            j = 0
            i = prev + 1
        return False
    
    def is_subString(self, root_list: list[str], sub_root_list: list[str]) -> bool:
        # build LPS 
        i = j = 0
        lps = [0] * len(sub_root_list)
        while i < len(sub_root_list):
            if sub_root_list[i] == sub_root_list[j] and i != 0:
                j += 1
                lps[i] = j
                i += 1
            elif j != 0:
                j = lps[j - 1]
            else:
                i += 1
        
        i = j = 0
        while i < len(root_list):
            if root_list[i] == sub_root_list[j]:
                i += 1
                j += 1
                if j == len(sub_root_list):
                    return True
            elif j != 0:
                j = lps[j - 1]
            else:
                i += 1
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # serilize the tree first
        # use kmp to do the matching
        root_list = self.serilize(root)
        sub_root_list = self.serilize(subRoot)
        return self.is_subString(root_list, sub_root_list)
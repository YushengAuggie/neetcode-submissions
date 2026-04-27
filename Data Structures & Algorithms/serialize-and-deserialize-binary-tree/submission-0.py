# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def helper(node: TreeNode) -> list[str]: 
            if not node:
                return ["#"]

            res = [str(node.val)]
            res.extend(helper(node.left))
            res.extend(helper(node.right))
            return res
        ret_list = helper(root)
        return ",".join(ret_list)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        list_data = data.split(",")
        if not list_data:
            return None
        idx = 0
        def helper() -> Optional[TreeNode]:
            nonlocal idx 
            if list_data[idx] == "#":
                idx += 1
                return None
            root_val = list_data[idx]
            idx += 1
            root = TreeNode(int(root_val))
            root.left = helper()
            root.right = helper()
            return root
        return helper()
    


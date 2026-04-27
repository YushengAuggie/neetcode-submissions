# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # bfs
        if not root:
            return ""
        ret_list = []
        queue = deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur is not None:
                ret_list.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                ret_list.append("#")
        return ",".join(ret_list)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if not vals:
            return None

        queue = deque()
        root = TreeNode(vals[0])
        queue.append(root)
        idx = 1
        while queue and idx < len(vals):
            prev_node = queue.popleft()
            cur_val = vals[idx]
            if cur_val != "#":
                cur_node = TreeNode(int(cur_val))
                prev_node.left = cur_node
                queue.append(cur_node)
            idx += 1
            
            cur_val = vals[idx]
            if cur_val != "#":
                cur_node = TreeNode(int(cur_val))
                prev_node.right= cur_node
                queue.append(cur_node)
            idx += 1
            
        return root


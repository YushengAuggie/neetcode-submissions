"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        cloned_node_dict = {} # node: cloned_node 
        
        def clone(node: Node) -> Optional[Node]:
            if not node:
                return

            if node in cloned_node_dict:
                return cloned_node_dict[node]

            cloned_node = Node(node.val)
            cloned_node_dict[node] = cloned_node
            for neighbor in node.neighbors:
                cloned_node.neighbors.append(clone(neighbor))
            return cloned_node
        return clone(node)

        

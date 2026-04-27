from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        valid tree:
        1. no cycle
        2. no independent node

        dfs: build a tree and go through all the node, and if re-visit a node, then cycle
            also need to check visited all the nodes
        
        Time(O(N + E)): all the edges and nodes
        Space(O(n)): all the nodes visited

        """
        visited = set()
        dict_directed_edges = defaultdict(list[int])

        for a, b in edges:
            dict_directed_edges[a].append(b)
            dict_directed_edges[b].append(a)
        
            
        def dfs(node: int, parent: int) -> bool:
            "Loop through the node."
            print(f"{node=}, {visited=}")
            if node in visited:
                # cycle
                print(cycle)
                return False
            else:
                visited.add(node)
                print(f"next: {dict_directed_edges[node]=}")
                for b in dict_directed_edges[node]:
                    if b == parent:
                        continue
                    if not dfs(b, node):
                        return False
            return True
        
        if dfs(0, -1):
            return len(visited) == n
        return False
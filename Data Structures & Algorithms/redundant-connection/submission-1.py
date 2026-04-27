class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        sort of like union find
        and 
        for node A and B
            we try to union them
            firstly we see if A's root (the smallest value in graph conncted to A or A's neighbors)
            and then we compare A's and B's root, and see whether they are the same, if they are the same, then this is the extra edge
        Time: O(n) n -> number of edges
        Space: O(m) m -> number of v
        """

        
        def union(a: int, b:int) -> bool:
            """
            Union A and B 
            return False if this forming a cycle
            """

            a_root = find(a)
            b_root = find(b)
            
            if a_root == b_root:
                return False
            
            if rank[a_root] > rank[b_root]:
                graph[b_root] = a_root
            elif rank[a_root] < rank[b_root]:
                graph[a_root] = b_root
            else:
                graph[b_root] = a_root
                rank[a] += 1
            return True
            
        def find(a:int) -> int:
            if a not in graph:
                graph[a] = a
                rank[a] = 0
            if graph[a] != a:
                graph[a] = find(graph[a])
            return graph[a]

        graph = {}
        rank = {}

        for a, b in edges:
            if not union(a, b):
                return [a, b]
        return []
            
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        sort of like union find
        and 
        for node A and B
            we try to union them
            firstly we see if A's root (the smallest value in graph conncted to A or A's neighbors)
            and then we compare A's and B's root, and see whether they are the same, if they are the same, then this is the extra edge
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
            
            if a_root < b_root:
                graph[b_root] = a_root
                find(b)
            else:
                graph[a_root] = b_root
                find(a)
            return True
            
        def find(a:int) -> int:
            if a not in graph:
                graph[a] = a
            if graph[a] != a:
                graph[a] = find(graph[a])
            return graph[a]

        graph = {}

        for a, b in edges:
            if not union(a, b):
                return [a, b]
        return []
            
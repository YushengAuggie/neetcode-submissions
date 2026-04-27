class UnionFind:
    def __init__(self, n:int) -> None:
        self.node_root = {}
        for i in range(n):
            self.node_root[i] = i
        self.clusters = n
    
    def find(self, a:int) -> int:
        """Return a's root."""
        if not self.node_root[a] == a:
            self.node_root[a] = self.find(self.node_root[a])
        return self.node_root[a]

    
    def union(self, a: int, b: int) -> int:
        p_a = self.find(a)
        p_b = self.find(b)

        if p_a == p_b:
            return p_a

        self.clusters -= 1
        if p_a > p_b:
            self.node_root[p_b] = p_a
            return p_a

        self.node_root[p_a] = p_b
        return p_b


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        typical union find problem 
        time: O(a(n)) -> almost O(n)
        space: O(n)


        create union find cluster for all the nodes, and finally, we check how many clusters
        """ 
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        print(uf.node_root)
            
        return uf.clusters


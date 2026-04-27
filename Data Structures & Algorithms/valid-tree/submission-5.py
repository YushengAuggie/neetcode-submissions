class Union:
    def __init__(self, n:int) -> None:
        self.cluster = {}
        self.rank =  [1] * n

    def find(self, a:int) -> int:
        if a not in self.cluster:
            self.cluster[a] = a
        else:
            if a != self.cluster[a]:
                self.cluster[a] = self.find(self.cluster[a])
        return self.cluster[a]
    
    def union(self, a: int, b:int) -> bool:
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            # cycle
            return False

        
        if self.rank[pa] > self.rank[pb]:
            self.cluster[pb] = self.cluster[pa]
            self.rank[pa] += self.rank[pb]
            self.rank[pb] = self.rank[pa]
        else:
            self.cluster[pa] = self.cluster[pb]
            self.rank[pb] += self.rank[pa]
            self.rank[pa] = self.rank[pb]
        return True

        

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Union find solution
        """
        if n - 1 != len(edges):
            return False

        union_find = Union(n)
        for c1, c2 in edges:
            if not union_find.union(c1, c2):
                return False
        print(union_find.cluster)
        print(union_find.rank)
        return True


        
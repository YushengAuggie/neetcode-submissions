from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cluster = 0
        visited = set()
        graph = defaultdict(list[int])

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(a:int) -> None:
            print(a, "in")
            if a in visited:
                return
            else:
                visited.add(a)
                print("add", a, visited)
                for b in graph[a]:
                    dfs(b)
            return
        
        for i in range(n):
            if i not in visited:
                print("new", i)
                dfs(i)
                cluster += 1
        return cluster
                
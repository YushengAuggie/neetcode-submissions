from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        topological sort

        """

        dependency_map = defaultdict(list[int])
        indegree = [0] * numCourses
        for c1, c2 in prerequisites:
            dependency_map[c2].append(c1)
            indegree[c1] += 1
        
        queue = []
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        
        took = 0
        while queue:
            cur = queue.pop()
            took += 1
            pres = dependency_map[cur] 
            for pre in pres:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    queue.append(pre)
            
        return took == numCourses



from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        So this is a graph problem
        Nodes are connected to each other with directed and weighted edges
        what we want is to find the shorest path that node k can reach all Nodes
        returns -1 if impossible

        let's assume there's no cycle first
        then we can use BFS to travel from source noce and then 
        there might be multiple ways to reach the same node
        so we will need an unique visited node 

        E: number of edges len(times)
        V: number of nodes

        time: O(ElogE)
        space: O(E + V)
        """

        visited = set()
        time = 0
        connections = defaultdict(list[list[int]])

        for a, b, w in times:
            connections[a].append([b, w])
        
        queue_with_time = []
        queue_with_time.append((0, k))
        heapq.heapify(queue_with_time)

        while queue_with_time and len(visited) < n:
            ready_time, cur = heapq.heappop(queue_with_time)
            if cur in visited:
                continue
            visited.add(cur)
            if ready_time > time:
                time = ready_time
            
            for next_node, travel_time in connections[cur]:
                if next_node not in visited:
                    heapq.heappush(
                        queue_with_time, (travel_time + ready_time, next_node)
                    )
        
        if len(visited) == n:
            return time
        else:
            return -1
            
            





        
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        BFS

        Firstly, we can build this graph (which we already have in the slides, but those are in the list).
        We want to have a dictionary to save from one point to another and their cost.
        Starting from one point, we want the potential next step we can take from there and its cost.

        enqueue src -> next step and enqueue -> reach dst or hit k
        return the min_cost

        time: O(min(E, k))
        space: O(min(E, k))

        """

        queue = []
        connections = defaultdict(list[tuple])
        cost_dict = {} # {station: cost} the smallest cost to reach station

        for a, b, price in flights:
            connections[a].append((b, price))
        
        queue = [(src, 0)] # dest, cost
        steps = 0
        while queue and steps <= k + 1:
            next_step_queue = []
            while queue:
                cur, cost = queue.pop()
                if cur in cost_dict and cost_dict[cur] <= cost:
                    continue
                cost_dict[cur] = cost
                if cur == dst:
                    continue
                for next_station, next_cost in connections[cur]:
                    next_step_queue.append((next_station, cost + next_cost))
            queue = next_step_queue
            steps += 1
        print(connections)
        print(cost_dict)
        return cost_dict.get(dst, -1)



            



        
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        So, we can start from the starting point, which is JFK. 
        Then, we just move to the next one. 


        So, what could go wrong here? 
        So, for example, if one start point has several different paths, 
        that means we need to make sure the paths can still reach all the other nodes.

        In this case, what we can do is use a DFS. Here, we need to make sure we do not take the same path again; meaning we can go back to the same point, but we cannot take the same path. We need to save the path into visited sets to avoid duplications.

        For this solution, we need to basically go over all the places and save them.

        1. Space: The space complexity will be O(N), where N is the number of nodes (like edges, or rather, the vectors).
        2. Time: The time complexity will be O(E). E is the number of edges, because we only take one edge at a time and we will not use duplications.

        """

        pathes = collections.defaultdict(list[str]) # key: source, value: list of destinations
        ticket_pathes = defaultdict(int) # pathes in tuples
        tickets.sort()
        remaining = len(tickets)
        
        for a, b in tickets:
            pathes[a].append(b)
            ticket_pathes[(a, b)] += 1
        
        # print(len(tickets))
        # lexicographically
        def dp(
            cur_path: list[str], cur: str, 
        ) -> list[str]:
            cur_path.append(cur)
            # print(visited_pathes)
            nonlocal remaining
            if remaining == 0:
                return cur_path
            
            for next_location in pathes[cur]:
                new_flight = (cur, next_location)
                if ticket_pathes[new_flight] > 0:
                    ticket_pathes[new_flight] -= 1
                    remaining -= 1
                    if ticket_pathes[new_flight] == 0:
                        del ticket_pathes[new_flight]
                    if valid_path := dp(cur_path, next_location):
                        return valid_path
                    ticket_pathes[new_flight] += 1
                    remaining += 1
            cur_path.pop()
            return []
        
        return dp([], "JFK")


        
        
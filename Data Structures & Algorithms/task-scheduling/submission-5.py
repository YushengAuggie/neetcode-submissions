import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        we can sort the tasks based on their occurance
        and then start sheduling those have higher counts
        and do greedy

        So the general complexity is:

        Time: O(T * k log k)
        Space: O(k)
        
        In this problem, since k <= 26, that becomes effectively:
        
        Time: O(T)
        Space: O(1))
        """
        count_dict = {}
        for task in tasks:
            if task not in count_dict:
                count_dict[task] = 0
            count_dict[task] += 1
        
        task_count_queue = [
            (-count, task) for task, count in count_dict.items()
        ]
        heapq.heapify(task_count_queue)

        last_occurance = {}
        index = 0
        while task_count_queue:
            need_idle = True
            next_round = []
            while task_count_queue:
                minor_count, task = heapq.heappop(task_count_queue)
                if index - last_occurance.get(task, float("-inf")) >= n + 1:
                    # valid
                    minor_count += 1
                    if minor_count < 0:
                        next_round.append((minor_count, task))
                    last_occurance[task] = index
                    index += 1
                    need_idle = False
                    break
                else:
                    next_round.append((minor_count, task))
                    # try next number
            if need_idle:
                index += 1
            for minor_count, task in next_round:
                heapq.heappush(task_count_queue, (minor_count, task))
        return index
            
            
            



        



        
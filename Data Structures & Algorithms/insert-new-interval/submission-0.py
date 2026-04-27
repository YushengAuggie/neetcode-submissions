class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Loop though the intervals List
        if overlap(lnew, ln):
            merge()
            check left and right
            everytime merge, check the same side
        
        compare n
        check overlap and merge and then keep merging n
        time: O(n)
        space: O(n)
        """

        def is_overlap(l1:list[int], l2:list[int]):
            s1, e1 = l1[0], l1[1]
            s2, e2 = l2[0], l2[1]

            return not bool(e1 < s2 or e2 < s1)
        merged_interval = []
        merged_idx = -1
        pre_small = False
        for idx, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                intervals.insert(idx, newInterval)
                break
        else:
            intervals.append(newInterval)
        
        print(intervals)
        res_internals = []
        prev = intervals[0]
        for interval in intervals[1:]:
            if is_overlap(interval, prev):
                print("overlap", interval, prev, end=" ")
                prev = [min(prev[0], interval[0]), max(prev[1], interval[1])]
                print("-> prev", prev)
            else:
                res_internals.append(prev)
                prev = interval
        res_internals.append(prev)
        return res_internals


        
        


                
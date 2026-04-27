class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort them -> nlogn 
        go through the list and merge intervals -> n

        time: O(n)
        space: O(n)
        """
    
        sorted_intervals = sorted(intervals)

        print(sorted_intervals)
        res = []
        prev = sorted_intervals[0]
        for idx, interval in enumerate(sorted_intervals):
            if idx == 0:
                continue
            print("cur", interval, "prev:", prev)
            if interval[0] > prev[1]:
                print("add", prev)
                res.append(prev)
                prev = interval
            else:
                # overlap, merge
                prev = [
                    prev[0],
                    max(prev[1], interval[1])
                ]
                print("merge prev", prev)
        res.append(prev)
        return res

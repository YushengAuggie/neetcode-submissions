class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        mem = {}
        intervals.sort()
        print(intervals)
        def dfs(idx:int, prev_idx: int) -> int:
            """
            @return the largest amount of intervals can get
            """

            if idx in mem:
                return mem[(idx, prev_idx)]
            
            if idx == len(intervals):
                return 0
            
            # skip
            res = dfs(idx + 1, prev_idx)

            # choose
            if prev_idx == -1 or intervals[idx][0] >= intervals[prev_idx][1]:
                res = max(res, 1 + dfs(idx + 1, idx))
            mem[(idx, prev_idx)] = res
            return res

        res = len(intervals) - dfs(0, -1)
        print(mem)
        return res
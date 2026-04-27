class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Brute force
        recursionally removing every interval from the list and see
        whether the list has overlappings
        time: O(2^n) 
        space: O(n)

        solution2
        Sort them and remove the largest interval each time
        time: O(nlogn)
        space: O(1)
        """

        intervals.sort()
        prev = intervals[0]
        count = 0
        print(intervals)
        for idx, interval in enumerate(intervals):
            if idx == 0:
                continue
            if interval[0] < prev[1]:
                # overlap, leave the one ends early
                if interval[1] < prev[1]:
                    print("remove ", prev)
                    prev = interval
                else:
                    print("remove ", prev)
                count += 1
            else:
                print("add", interval)
                prev = interval
        return count
            




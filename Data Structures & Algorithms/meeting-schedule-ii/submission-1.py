"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x: (x.start, x.end))
        count = 1
        rooms = [intervals[0].end]


        for interval in intervals[1:]:
            while rooms and rooms[0] <= interval.start:
                # not overlap with the new one
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
            count = max(count, len(rooms))
        return count



                
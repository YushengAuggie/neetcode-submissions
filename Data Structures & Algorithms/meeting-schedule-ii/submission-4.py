"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Time: nlogn
        Space: n
        """
        meetings = defaultdict(int)
        for i in intervals:
            meetings[i.start] += 1
            meetings[i.end] -= 1

        count = 0
        on_going = 0
        for i in sorted(meetings.keys()):
            on_going += meetings[i]
            count = max(count, on_going)
        return count
        
        
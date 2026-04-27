"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, x.end))
        prev_end = -1
        for interval in intervals:
            if interval.start < prev_end:
                return False
            else:
                prev_end = interval.end
        return True

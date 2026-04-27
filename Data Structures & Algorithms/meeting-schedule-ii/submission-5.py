"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        s, e = 0, 0
        on_going = 0
        count = 0 

        while s < len(starts) and e < len(ends):
            if starts[s] < ends[e]:
                # overlap
                on_going += 1
                count = max(count, on_going)
                s += 1
            else:
                on_going -= 1
                e += 1
        return count


        

        
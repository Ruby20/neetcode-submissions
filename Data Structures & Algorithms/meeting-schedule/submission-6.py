"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True

        # sort the intervals
        intervals.sort(key = lambda i: i.start)

        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur.start < prev.end:
                return False
            prev = cur 
        
        return True         
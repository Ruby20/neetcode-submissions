"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i:i.start)    
        n = intervals[0]
        for i in range(1, len(intervals)):
            c = intervals[i]
            if c.start < n.end:
                return False
            n = c    
        return True         


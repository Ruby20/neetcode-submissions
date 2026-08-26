"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0
        
        intervals.sort(key = lambda i: i.start)
        heap = []

        n = intervals[0]
        heapq.heappush(heap, n.end)

        for i in range(1, len(intervals)):
            c = intervals[i]

            if c.start >= heap[0]:
                heapq.heappop(heap)
            n = c
            heapq.heappush(heap, c.end)

        return len(heap)        



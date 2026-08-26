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
        # sort the list by start time
        intervals.sort(key = lambda i: i.start)
        heap = []
        n = intervals[0]
        heapq.heappush(heap, n.end)

        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur.start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, cur.end)

        return len(heap)


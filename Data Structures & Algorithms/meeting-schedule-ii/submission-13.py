"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sweep line algo
        rooms = defaultdict(int)
        for i in intervals:
            rooms[i.start] += 1
            rooms[i.end] -= 1 
        
        prev = 0
        res = 0

        for i in sorted(rooms.keys()):
            prev += rooms[i]
            res = max(res, prev)

        return res





        # # min heap approach
        # intervals.sort(key = lambda x: (x.start))
        # rooms = []

        # for interval in intervals:
        #     if rooms and rooms[0] <= interval.start:
        #         heapq.heappop(rooms)
        #     heapq.heappush(rooms, interval.end)


        # return  len(rooms)
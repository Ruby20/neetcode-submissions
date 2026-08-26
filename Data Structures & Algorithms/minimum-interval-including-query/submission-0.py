class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,7,6,8]
        # sort the intervals
        intervals.sort()
        # visit the queries in sorted order?
        # heap to maintain the end times corresponding to the queries
        # minheap -> (size, end_time)  coz we want the min interval range that query belongs to
        i = 0
        minheap = []
        res = {} # hashmap
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minheap, (r - l + 1, r))
                i += 1

            while minheap and minheap[0][1] < q:
                    heapq.heappop(minheap)

            res[q] = minheap[0][0] if minheap else -1
        
        return  [res[q] for q in queries]

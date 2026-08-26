class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calc the euclid distance from origin
        minheap = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(minheap, (dist, [x, y]))
        
        heapq.heapify(minheap)
        # put the points and dist to heap


        # pop k closest points
        res = []
        while minheap:
            dist, [x, y] = heapq.heappop(minheap)
            res.append([x, y])
            if len(res) == k:
                return res

        
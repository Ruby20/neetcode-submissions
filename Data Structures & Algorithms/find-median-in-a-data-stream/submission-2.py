class MedianFinder:
    # TWo heaps
    # median in a data stream
    # find max min is O(1)
    # adding and removing is O(n)

    def __init__(self):
        self.smallheap = []
        self.largeheap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallheap, -1 * num)
        
        # every element small heap <= large heap
        if (self.smallheap and self.largeheap 
            and (-1 * self.smallheap[0]) > self.largeheap[0]):
                val = heapq.heappop(self.smallheap)
                heapq.heappush(self.largeheap, -1 * val)

        # heaps should be of approx equal size
        if len(self.smallheap) > len(self.largeheap) + 1:
            val = heapq.heappop(self.smallheap)
            heapq.heappush(self.largeheap, -1 * val)

        if len(self.largeheap) > len(self.smallheap) + 1:
            val = heapq.heappop(self.largeheap)
            heapq.heappush(self.smallheap, -1 * val)
        

    def findMedian(self) -> float:
        if len(self.smallheap) > len(self.largeheap):
            return -1 * self.smallheap[0] 
        if len(self.largeheap) > len(self.smallheap):
            return self.largeheap[0]
        return (-1 * self.smallheap[0] + self.largeheap[0]) / 2
        
        
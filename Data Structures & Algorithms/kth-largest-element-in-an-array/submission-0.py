class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solve using minheap
        # store k elements in the heap
        minheap = nums[:k]
        heapq.heapify(minheap)

        for n in nums[k:]:
            heapq.heappush(minheap, n)
            heapq.heappop(minheap)
        return minheap[0]    


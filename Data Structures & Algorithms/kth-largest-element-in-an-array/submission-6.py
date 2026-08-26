import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minheap = nums[:k]
        heapq.heapify(minheap)
        
        for i in range(k, len(nums)):
            heapq.heappush(minheap, nums[i])
            heapq.heappop(minheap)
            print(nums[i], minheap)
        return minheap[0]    



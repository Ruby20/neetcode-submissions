class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap solution
        pq = nums[:k]
        heapq.heapify(pq)

        for i in range(k, len(nums)):
            heapq.heappush(pq, nums[i])
            heapq.heappop(pq)

        return pq[0]    

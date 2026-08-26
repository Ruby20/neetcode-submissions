class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums[:k]
        heapq.heapify(minheap)

        n = len(nums)
        for num in nums[k:]:
            heapq.heappush(minheap, num)
            heapq.heappop(minheap)
            
        return  minheap[0]       




        
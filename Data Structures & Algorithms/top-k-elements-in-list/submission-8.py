class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        buckets = {}

        for i in range(len(nums)):
            key = nums[i]
            if key in buckets:
                buckets[key] += 1
            else:    
                buckets[key] = 1

        buffer = []
        for num, cnt in buckets.items():
            buffer.append([cnt, num])
        buffer.sort()    

        res = []
        while len(res) < k:
            res.append(buffer.pop()[1])  

        return res    



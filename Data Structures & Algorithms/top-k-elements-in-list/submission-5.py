class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # use bucket sort 
        n = len(nums)
        bucket = [[] for i in range(n +1)]
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, c in count.items():
            bucket[c].append(num) 
        
        print(bucket)
        res = []
       
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
             

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort Approach
        
        # Map contains: (nums -> freq)
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        # buckets to invert the freq -> nums for Top k freq items
        buckets = [[] for i in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # iterate in reverse order to get top k
        # stop before 0
        res = []
        for i in range(len(buckets) - 1, 0, -1):    
            for b in buckets[i]:
                res.append(b)
                if len(res) == k:
                    return res

        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda i:i[0])
        n = intervals[0]

        for i in range(1,len(intervals)):
            cur = intervals[i]
            if cur[0] > n[1]: # no overlap
                res.append(n)
                n = cur
            elif cur[0] <= n[1]: # handle overlap
                n[0] = min(cur[0], n[0])
                n[1] = max(cur[1], n[1])
     
        
        res.append(n)
        return res
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for int_idx in range(len(intervals)):
            if newInterval[1] < intervals[int_idx][0]:
                res.append(newInterval)
                return res + intervals[int_idx:]
            elif newInterval[0] >  intervals[int_idx][1]:  
                res.append(intervals[int_idx])
            else:
                newInterval[0] = min(newInterval[0], intervals[int_idx][0])    
                newInterval[1] = max(newInterval[1], intervals[int_idx][1])    
        res.append(newInterval)
        return res



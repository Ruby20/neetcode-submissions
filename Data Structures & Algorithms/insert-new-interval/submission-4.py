class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert new interval in a sorted list of intervals
        # identify overlaps and merge
        res = []

        for idx in range(len(intervals)):
            if newInterval[1] < intervals[idx][0]:
                res.append(newInterval)
                return res + intervals[idx: ]
            elif newInterval[0] > intervals[idx][1]:
                res.append(intervals[idx])
            else:
                newInterval[0] = min(newInterval[0], intervals[idx][0])     
                newInterval[1] = max(newInterval[1], intervals[idx][1])
        res.append(newInterval)    
        return res
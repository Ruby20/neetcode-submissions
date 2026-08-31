class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.append(newInterval)
        # intervals.sort()
        # merged = []
        # do not sort again as the lsit is already sorted

        res = []
        for idx in range(len(intervals)):
            if newInterval[1] < intervals[idx][0]:
                res.append(newInterval)
                return res + intervals[idx: ] # imp to return the list since the task is done!
            elif newInterval[0] > intervals[idx][1]:
                res.append(intervals[idx])
            else:
                newInterval[0] = min(newInterval[0], intervals[idx][0])
                newInterval[1] = max(newInterval[1], intervals[idx][1])
        res.append(newInterval)
        return res        

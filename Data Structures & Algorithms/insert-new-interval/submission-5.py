class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            # no overlap can insert the newinterval
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i: ]
                # no overlap so can insert intervals into res list
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])    
                newInterval[1] = max(newInterval[1], intervals[i][1])    

        res.append(newInterval)
        return res        


        
        
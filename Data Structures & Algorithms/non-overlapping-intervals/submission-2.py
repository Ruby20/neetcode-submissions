class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0
        
        intervals.sort(key=lambda i: i[1])   
        # print(intervals)     
        end = float('-inf') 
        count = 0

        for interval in intervals:
            # If the current interval does not overlap with the last one we kept
            # print(interval[0], end)
            if interval[0] >= end:
                # Update the end to be the end of the current interval
                end = interval[1]
            else:
                # Increment the count of intervals we need to remove
                count += 1

        return  count     


        
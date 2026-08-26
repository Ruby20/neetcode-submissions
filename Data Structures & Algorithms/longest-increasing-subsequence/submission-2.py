import bisect
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        tail = []
        for n in nums:

            index = bisect.bisect_left(tail, n)

            if index == len(tail):
                tail.append(n)
            else:
                tail[index] = n
        # print(tail) 
        return len(tail)            
        
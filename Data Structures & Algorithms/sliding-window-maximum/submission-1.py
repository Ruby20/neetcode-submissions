class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = right = 0 
        q = collections.deque()

        output = []

        while right < len(nums):
            # pop smaller elements form q
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right) # append the index

            # remove left from window    
            if left > q[0]:
                q.popleft()

            # window size
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
            right += 1
        return output        
                



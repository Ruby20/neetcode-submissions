class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return the max in each window
        # use deque
        left = right = 0
        q = deque()
        res = []

        # store the indexes in the q
        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:     # we have moved left; slide the window
                q.popleft()
            
            if (right + 1) >= k: # the window we want
                res.append(nums[q[0]]) # put it into the res
                left += 1 
            right += 1 
            
        return res    

# O(n)
# O(n)
        

        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()

        left = 0
        right = 0
        res = []

        while right < len(nums):

            # keep popping from right if we see greater element
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)    

            if left > q[0]:
                q.popleft()

            if (right + 1) >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1
        return res        


        
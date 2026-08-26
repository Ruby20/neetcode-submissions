class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 D soln DP
        rob1, rob2 = 0, 0
        for n in nums:
            temp = rob1
            rob1 = max(rob1, n + rob2)
            rob2 = temp
        return rob1

            #  TC: O(N) SC: O(1)
        
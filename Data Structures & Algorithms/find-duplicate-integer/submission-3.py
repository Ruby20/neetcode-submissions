class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # same as ll cycle 2 prob
        fast = 0
        slow = 0

        while fast < len(nums):
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow     


        
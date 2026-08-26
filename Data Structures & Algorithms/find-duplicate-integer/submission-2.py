class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # do not use extra space and do not modify the given list
        # we need to find the start of a cyle
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # we have a cycle; we need the head of the cycle detection
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow2        


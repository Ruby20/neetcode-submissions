class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # iterative approach
        res = [[]]

        for n in nums:
            nextperm = []
            for p in res:
                for i in range(len(p) + 1):
                    pcopy = p[:]
                    pcopy.insert(i, n)
                    nextperm.append(pcopy)
            res = nextperm        
        return res    
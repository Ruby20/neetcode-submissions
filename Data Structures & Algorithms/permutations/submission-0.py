class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]

        for n in nums:
            nextperms = []
            for p in perms:
                for i in range(len(p) + 1): # expanding list of perms coz we insert elem at pos
                    pcopy = p[:]
                    pcopy.insert(i, n)
                    nextperms.append(pcopy)
            perms = nextperms
        return perms            

        
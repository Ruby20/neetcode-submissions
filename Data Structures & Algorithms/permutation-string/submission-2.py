class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        sCount = [0] * 26
        pCount = [0] * 26

        for i in range(len(s1)):
            pCount[ord(s1[i]) - ord('a')] += 1
            sCount[ord(s2[i]) - ord('a')] += 1

        # sliding window
        left = 0
        
        
        for right in range(len(s1), len(s2)):
            if pCount == sCount:
                return True
            index = ord(s2[right]) - ord("a")
            sCount[index] += 1
            
            index = ord(s2[left]) - ord("a")
            sCount[index] -= 1    
            left += 1

        if pCount == sCount:
            return True    
            
        return False
        
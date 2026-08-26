class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # use a hashmap
        count_s = {}
        for l in s:    
            if l in count_s:
                count_s[l] += 1
            else:    
                count_s[l] = 1

        
        for l in t:
            if l in count_s:
                count_s[l] -= 1
            else:
                return False

        for val in count_s.values():
            if val != 0:
                return False

        return True        


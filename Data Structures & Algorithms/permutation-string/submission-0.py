class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window with hashmap
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        matched = 0    

        for  i in range(26):
            if s1Count[i] == s2Count[i]:
                matched += 1

        # start sliding
        left = 0
        for right in range(len(s1), len(s2)):
            if matched == 26:
                return True
            # match the right chars with s1Count    
            index = ord(s2[right]) - ord('a')
            s2Count[index] += 1

            if s2Count[index] == s1Count[index]:
                matched += 1
            elif s2Count[index] == s1Count[index] + 1:
                matched -= 1


            # compare the left char in the window
            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1 # chop off left char
            if s2Count[index] == s1Count[index]:
                matched += 1
            elif s2Count[index]  == s1Count[index] - 1:
                matched -= 1
            left += 1    
        return matched == 26        




        
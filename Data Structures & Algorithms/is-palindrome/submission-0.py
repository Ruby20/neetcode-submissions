class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        i, j = 0, len(s)-1

        # check for lowercase and if char is alpha numeric
        while i < j:
            if not s[i].isalnum():
               i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                
                i , j = i+1, j-1    
        return True        


        
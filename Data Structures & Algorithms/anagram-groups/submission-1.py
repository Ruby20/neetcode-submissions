class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap and sort the keys

        anagram = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in anagram:
                anagram[key].append(s)
            else:    
                anagram[key] = [s]

        res = []
        
        for key, val in anagram.items():
            res.append(val)

        # print(res)
        return res    



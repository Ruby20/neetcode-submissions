class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort the strs and add to hashmap
        anaMap = {}
        res = []

        for s in strs:
            key = ''.join(sorted(s))
            if key not in anaMap:
                anaMap[key] = [s]
            else:    
                anaMap[key].append(s)

        for key, val in anaMap.items():
            res.append(val)

        return res            


        
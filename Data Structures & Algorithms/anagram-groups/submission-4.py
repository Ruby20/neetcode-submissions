class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashtable with arrays
        # kv ? char freq tuple -> words that map to the char freq arr
        # mapping of the 
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # char arr
            for char in s:
                count[ord(char) - ord('a')] += 1
            # convert the char freq arr into a tuple key - immutable
            res[tuple(count)].append(s)
        
        return list(res.values())        
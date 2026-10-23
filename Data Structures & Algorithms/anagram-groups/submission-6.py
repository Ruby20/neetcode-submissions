class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            char_arr = [0] * 26
            for char in word:
                char_arr[ord(char) - ord('a')] += 1
            res[tuple(char_arr)].append(word)
        return list(res.values())

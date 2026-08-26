class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use hashmap and arrays
        # use char arrays tuples??
        # tuple char arr as the key??

        word_map = defaultdict(list)
        res = []
        for word in strs:
            ch_arr = [0] * 26
            for char in word:
                ch_arr[ord(char) - ord('a')] += 1
            word_map[tuple(ch_arr)].append(word)

        return list(word_map.values())

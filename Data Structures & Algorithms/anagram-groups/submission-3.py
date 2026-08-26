class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # bucket sort
        buckets = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            buckets[tuple(count)].append(word)

        res = []
        for values in buckets.values():
            res.append(values)
        return res     
    # Time: O(N * M)
    # space: O(M) where M is the num of strings and n is the longest string

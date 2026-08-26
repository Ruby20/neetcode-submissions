class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {} # -> char, lastindex
        for i, c in enumerate(s):
            last_idx[c] = i

        size = 0 
        end = 0
        partition = []

        for i, c in enumerate(s):
            size += 1

            if last_idx[c] > end:
                end = last_idx[c]

            if i == end:
                partition.append(size)
                size = 0

        return partition        












        
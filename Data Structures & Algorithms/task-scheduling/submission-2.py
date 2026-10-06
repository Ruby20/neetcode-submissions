class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # hashmap to get the count of tasks
        # there is no execution order
        # 1 - heap and hashmap
        # 2 - hashmap and greedy optimization

        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        freq.sort()
        maxf = freq[25]
        idle_slots = (maxf - 1) * n

        for i in range(24, -1, -1):
            idle_slots -= min(freq[i], maxf - 1)

        return len(tasks) + max(idle_slots, 0)


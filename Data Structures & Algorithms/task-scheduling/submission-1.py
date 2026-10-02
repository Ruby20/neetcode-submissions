class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # greedy makes more sense than the heap solution
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        count.sort() 
        maxf = count[25]
        idle = (maxf - 1) * n

        # fill up other tasks in the idle slots
        for i in range(24, -1, -1):
            idle -= min(count[i], maxf - 1)

        return max(0, idle) + len(tasks)    
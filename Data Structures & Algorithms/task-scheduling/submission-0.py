class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count the number of tasks
        freq = Counter(tasks)
        
        # store task freq list as a maxheap
        maxheap = [-cnt for cnt in freq.values()] # -ve because of Python
        heapq.heapify(maxheap)
        
        # queue up tasks that need to run after idle time
        q = deque()

        time = 0
        while maxheap or q:
            time += 1
            if maxheap:
                taskf = heapq.heappop(maxheap) # decrement the count
                taskf += 1
                if taskf:
                    q.append([taskf, time + n])

            if q and q[0][1] == time:
                t = q.popleft()[0]
                heapq.heappush(maxheap, t)

        return time        










        
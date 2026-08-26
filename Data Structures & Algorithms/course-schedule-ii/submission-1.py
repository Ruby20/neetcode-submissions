class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort Algorithm
        prereq = {i: [] for i in range(numCourses)}

        for cr, pre in prerequisites:
            prereq[cr].append(pre)

        cycle = set()
        visit = set()
        output = [] # order of the courses

        def dfs(cr):
            if cr in cycle:
                return False
            if cr in visit:
                return True
            cycle.add(cr)

            for pre in prereq[cr]:
                if not dfs(pre):
                    return False
            cycle.remove(cr)
            visit.add(cr)
            output.append(cr)
            return True

        for c in range(numCourses):            
            if not dfs(c):
                return []
        return output        

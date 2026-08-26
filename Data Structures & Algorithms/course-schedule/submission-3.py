class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # hashmap of prereqs
        prereq_map = {n : [] for n in range(numCourses) }

        # populate map
        for crs, pre in prerequisites:
            prereq_map[crs].append(pre)

        visit = set()    

        # dfs
        def dfs(crs):
            # base cases
            if prereq_map[crs] == []:
                return True

            if crs in visit:
                return False

            # visit the prereqs
            visit.add(crs)
            for prereqs in prereq_map[crs]:
                if not dfs(prereqs):
                    return False

            visit.remove(crs)
            prereq_map[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True        


        
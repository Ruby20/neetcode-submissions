class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {n : [] for n in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        visiting = set()

        def dfs(cr):
            if cr in visiting:
                return False
            if prereq[cr] == []:
                return True
            visiting.add(cr)

            for pre in prereq[cr]:
                if not dfs(pre):
                    return False

            visiting.remove(cr)
            prereq[cr] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True                    


        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build a prereqmap
        prereqmap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereqmap[crs].append(pre)

        visit = set()
        cycle = set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereqmap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs) # why? no longer along the path
            visit.add(crs)
            output.append(crs)      
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output        
        
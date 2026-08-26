class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dims
        rows, cols = len(heights), len(heights[0])
        # two sets of visiting nodes
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
                r == rows or c == cols or
                min(r, c) < 0 or
                heights[r][c] < prevHeight):
                    return
            visit.add((r, c))        
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        # get all cols closer to pac and atl
        for c in range(cols):
            # 0, c is closer to pacific
            dfs(0, c, pac, heights[0][c])
            # atl
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # get all dims closer to pac and atl changing the rows
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        # check if r, c present in both sets
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        return res




        
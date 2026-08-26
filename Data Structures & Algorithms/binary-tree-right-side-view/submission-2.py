# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # use BFS algorithm
        seen = deque()
        res = []

        if not root:
            return res

        seen.append(root)
        level = 0

        while len(seen) > 0:
            rightval = None
            for i in range(len(seen)):
                cur = seen.popleft()
                rightval = cur
                if cur.left:
                    seen.append(cur.left)
                if cur.right:
                    seen.append(cur.right)    
            level += 1
            if rightval:
                res.append(rightval.val)

        return res        

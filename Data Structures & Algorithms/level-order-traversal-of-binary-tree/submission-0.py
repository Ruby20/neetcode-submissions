# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        seen = deque()
        res = []

        if root:
            seen.append(root)

        while len(seen) > 0:
            row = []
            for i in range(len(seen)):
                cur = seen.popleft()    
                row.append(cur.val)
                if cur.left:
                    seen.append(cur.left)
                if cur.right:
                    seen.append(cur.right)
            res.append(row)

        return res                


        
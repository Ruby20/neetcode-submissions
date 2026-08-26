# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def depth(cur):
            if not cur:
                return 0
            left = depth(cur.left)
            right = depth(cur.right)

            self.result = max(self.result, left + right)
            return 1 + max(left, right)    

        depth(root)
        return self.result
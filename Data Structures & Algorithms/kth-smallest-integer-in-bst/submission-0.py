# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        res = self.inorder(root)
        for i in range(len(res)):
            if k-1 == i:
                return res[i]





    def inorder(self, root: Optional[TreeNode]):
        res = []
        if root.left:
            res+= self.inorder(root.left)
        res.append(root.val)
        if root.right:
            res+= self.inorder(root.right)
        return res 
        
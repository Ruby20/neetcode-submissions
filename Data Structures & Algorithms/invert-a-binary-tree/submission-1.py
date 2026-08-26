# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp1 = self.invertTree(root.left)
        temp2 = self.invertTree(root.right)

        root.right = temp1
        root.left = temp2

        return root





        
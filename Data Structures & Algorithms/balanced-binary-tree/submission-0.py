# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.height(root) >= 0) 
        

    def height(self, root: Optional[TreeNode]) -> int :
        if not root:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)

        if lheight < 0 or rheight < 0 or abs(lheight-rheight) > 1:
            return -1

        return max(lheight, rheight) + 1    

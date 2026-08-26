# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # helper height func
        # recurisvely calc height and check
        # if lheight < 0, rheight < 0 
        # or height diff > 1
        def height(root):
            if not root:
                return 0

            lheight = height(root.left)
            rheight = height(root.right)

            if lheight < 0 or rheight < 0 or abs(lheight - rheight) > 1:
                return -1
                
            return max(lheight, rheight) + 1    

        return height(root) >= 0        
        
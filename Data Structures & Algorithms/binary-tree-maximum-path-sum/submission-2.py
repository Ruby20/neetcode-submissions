# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] # written this way so that we can modify it within the recursive func

        def helper(node):
            if not node:
                return 0

            # we could have -ve values in the path, so we ignore them
            leftMax = max(0, helper(node.left))    
            rightMax = max(0, helper(node.right))

            res[0] = max(res[0], node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax) 


        helper(root)
        return res[0]    
        
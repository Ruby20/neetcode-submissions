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

        def dfs(node):
            if not node:
                return None
                
            if not node.left and not node.right:
                return node
            left = dfs(node.left)
            right = dfs(node.right)

            node.right = left
            node.left = right

            return node    

        dfs(root)
        return root    
        
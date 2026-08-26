# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(node, max_val):
            nonlocal count 
            if not node:
                return 0

            if node.val >= max_val:
                max_val = node.val
                count += 1

            # if not node.left and not node.right:

            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)

            return max(left, right)

        dfs(root, root.val)
        # print(ans)
        return count    






        
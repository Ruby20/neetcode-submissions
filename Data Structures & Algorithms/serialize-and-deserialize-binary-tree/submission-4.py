# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # bfs or dfs
        if not root:
            return "N"

        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if not node:
                res.append("N")
            else:
                # print(str(node.val))
                res.append(str(node.val))
                q.append(node.left)    
                q.append(node.right)

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        current = data.split(",")
        if current[0] == "N":
            return None

        root = TreeNode(int(current[0]))    
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            if current[index] != "N":
                node.left = TreeNode(int(current[index])) 
                q.append(node.left)
            index += 1
            
            if current[index] != "N":
                node.right = TreeNode(int(current[index])) 
                q.append(node.right)
            index += 1        
        return root     








# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    null = "#"
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = ""
        if not root:
            return ans

        def dfs(root):
            nonlocal ans
            if not root:
                ans += self.null + ","
                return
            ans += str(root.val) + ","
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return ans[:-1]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if vals[i] == self.null:
                i += 1
                return None
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

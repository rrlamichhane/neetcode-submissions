# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root]
        while q:
            q_len = len(q)
            level = []
            for i in range(q_len):
                node = q[i]
                if node:
                    level.append(node)
            q = []
            l_val = []
            for l in level:
                l_val.append(l.val)
                q.append(l.left)
                q.append(l.right)
            if l_val:
                res.append(l_val)
        return res

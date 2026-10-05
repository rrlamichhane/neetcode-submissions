# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        ans = []

        while q:
            q_len = len(q)
            cur_level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    cur_level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            ans.append(cur_level) if cur_level else None
            
        return ans

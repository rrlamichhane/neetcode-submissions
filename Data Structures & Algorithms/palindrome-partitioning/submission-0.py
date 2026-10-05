class Solution:
    def is_palindrome(self, s,l ,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        partition = []

        def dfs(i):
            if i >= len(s):
                ans.append(partition.copy())
                return
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()

        dfs(0)
        return ans

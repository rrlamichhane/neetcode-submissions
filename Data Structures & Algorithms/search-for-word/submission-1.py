class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        tr, tc = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= tr or c >= tc or (r, c) in visited or word[i] != board[r][c]:
                return False
            visited.add((r,c))
            i += 1
            res = dfs(r+1, c, i) or dfs(r-1, c, i) or dfs(r, c+1, i) or dfs(r, c-1, i)
            visited.remove((r,c))
            return res
        
        for r in range(tr):
            for c in range(tc):
                res = dfs(r, c, 0)
                if res:
                    return True
        return False

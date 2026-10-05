class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal num_islands
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    num_islands += 1
        
        dfs(0, 0)
        return num_islands

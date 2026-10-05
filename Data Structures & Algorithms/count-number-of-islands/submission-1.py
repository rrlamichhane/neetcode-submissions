class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, cur_island):
            if min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == "0":
                return 
           
            visited.add((r,c))
            dfs(r+1, c, cur_island)
            dfs(r-1, c, cur_island)
            dfs(r, c+1, cur_island)
            dfs(r, c-1, cur_island)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c, [])
                    islands += 1
        
        return islands
        
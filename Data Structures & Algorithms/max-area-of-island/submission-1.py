class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            nonlocal visited, max_area
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            cur_area = 1
            for i, j in directions:
                cur_area += dfs(r+i, c+j)
            return cur_area
        
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area

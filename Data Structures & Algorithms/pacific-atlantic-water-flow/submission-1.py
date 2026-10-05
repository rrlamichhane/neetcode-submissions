class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        flows_to_atlantic = set()
        flows_to_pacific = set()
        directions = ((1,0), (-1,0), (0,1), (0,-1))

        inside_bounds = lambda r, c: r >= 0 and c >= 0 and r < rows and c < cols

        def dfs(r, c, visited, prev_height):
            if ((r,c) in visited or not inside_bounds(r,c) or heights[r][c] < prev_height):
                return
            visited.add((r, c))
            for i, j in directions:
                dfs(r+i, c+j, visited, heights[r][c])
        
        # DFS for boundary rows
        for c in range(cols):
            dfs(0, c, flows_to_pacific, heights[0][c])
            dfs(rows-1, c, flows_to_atlantic, heights[rows-1][c])
        
        # DFS for boundary columns
        for r in range(rows):
            dfs(r, 0, flows_to_pacific, heights[r][0])
            dfs(r, cols-1, flows_to_atlantic, heights[r][cols-1])

        return list(flows_to_atlantic & flows_to_pacific)

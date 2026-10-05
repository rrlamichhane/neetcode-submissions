class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                cur_r, cur_c = q.popleft()
                grid[cur_r][cur_c] = dist
                for i, j in directions:
                    r = cur_r + i
                    c = cur_c + j
                    if (min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == -1):
                        continue
                    visited.add((r,c))
                    q.append((r,c))
            dist += 1

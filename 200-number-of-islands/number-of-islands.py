class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        seen = set()

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r, c):
            q = deque()
            seen.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and (nr, nc) not in seen and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        seen.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands += 1
        return islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) # length of rows, length of cols
        
        def dfs(i, j):
            # edge cases: if row index is too high, out of bounds going down, out of bounds to the left, out opf bounds to the right, 
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            else: # it is a valid postion then mark it as 0 and do dfs going in all directions
                grid[i][j] = '0'
                dfs(i, j+1) # on the right
                dfs(i+1, j) # on the bottom
                dfs(i, j-1) # on the left
                dfs(i-1, j) # on the top
                 
        num_islands = 0
        # traverse matrix going left to right
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
                    
        return num_islands
    
    # Time: O(m * n)
    # Space: O(m * n)
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def numOfIslands(grid):
            def dfs(i,j):
                if not vis[i][j]:
                    vis[i][j] = True
                    for dx,dy in dir:
                        x,y = i+dx,j+dy
                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1:
                            dfs(x,y)
            dir = [(0,1),(1,0),(0,-1),(-1,0)]
            vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
            res = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if not vis[i][j] and grid[i][j]==1:
                        dfs(i,j)
                        res += 1
            return res 
        
        moves = 0

        # edge case
        if numOfIslands(grid)!=1:
            return moves
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    grid[i][j] = 0
                    if numOfIslands(grid)!=1:
                        return 1
                    grid[i][j] = 1
        return 2 
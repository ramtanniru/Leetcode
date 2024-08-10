class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def numberOfIslands(grid):
            def dfs(i,j):
                if not vis[i][j]:
                    vis[i][j] = True
                    for dx,dy in dir:
                        x,y = i+dx,j+dy
                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1:
                            dfs(x,y)
            vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
            dir = [(0,1),(1,0),(0,-1),(-1,0)]
            numOfIslands = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if not vis[i][j] and grid[i][j]==1:
                        numOfIslands += 1
                        dfs(i,j)
            return numOfIslands 

        mat = [[1 for i in range(3*len(grid[0]))] for j in range(3*len(grid))]
        i = 0
        while i<len(grid):
            j = 0
            while j<len(grid[0]):
                if grid[i][j]!=" ":
                    if grid[i][j]=='/':
                        mat[3*i][3*j + 2] = 0
                        mat[3*i + 1][3*j + 1] = 0
                        mat[3*i + 2][3*j] = 0
                    else:
                        mat[3*i][3*j] = 0
                        mat[3*i + 1][3*j + 1] = 0
                        mat[3*i + 2][3*j + 2] = 0
                j+=1
            i+=1
        return numberOfIslands(mat) 
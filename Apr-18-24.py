class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        per = 0
        l,b = len(grid),len(grid[0])
        for i in range(l):
            for j in range(b):
                if grid[i][j]==1:
                    per += 4
                    if i>0 and grid[i-1][j]==1:
                        per -= 1
                    if j>0 and grid[i][j-1]==1:
                        per -= 1
                    if i<l-1 and grid[i+1][j]==1:
                        per -= 1
                    if j<b-1 and grid[i][j+1]==1:
                        per -=1
        return per
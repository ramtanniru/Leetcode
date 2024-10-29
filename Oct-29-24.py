class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def rec(i,j):
            if j==len(grid[0])-1:
                return 0
            if dp[i][j]!=-1: return dp[i][j]
            dir = [(0,1),(-1,1),(1,1)]
            ans = 0
            for dx,dy in dir:
                x,y= i+dx,j+dy
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[i][j]<grid[x][y]:
                    ans = max(ans,1+rec(x,y))
            dp[i][j] = ans
            return dp[i][j]
        ans = 0
        dp = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            ans = max(ans,rec(i,0))
        return ans
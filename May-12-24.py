class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        l = []
        n = len(grid)
        for i in range(n-2):
            k = []
            for j in range(n-2):
                k.append(max(
                    max(grid[i][j:j+3]),
                    max(grid[i+1][j:j+3]),
                    max(grid[i+2][j:j+3])
                    ))
            l.append(k)
        return l
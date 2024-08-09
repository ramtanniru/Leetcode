class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(grid):
            s = sum(grid[0])
            hash = set()
            for i in grid:
                for j in i:
                    if not 0<j<=9:
                        return False
                    hash.add(j)
            if len(hash)!=9:
                return False
            # row
            for i in grid:
                if sum(i)!=s:
                    return False
            # col
            for i in range(3):
                colSum = 0
                for j in range(3):
                    colSum += grid[j][i]
                if colSum!=s:
                    return False
            # diagonal
            if grid[0][0]+grid[1][1]+grid[2][2]!=s or grid[0][2]+grid[1][1]+grid[2][0]!=s:
                return False
            return True

        if len(grid)<3 or len(grid[0])<3:
            return 0
        cnt = 0
        t,b = 0,3
        while t<=len(grid)-3:
            l,r = 0,3
            while l<=len(grid[0])-3:
                temp = [[0 for i in range(3)] for i in range(3)]
                x = 0
                for i in range(t,b):
                    y = 0
                    for j in range(l,r):
                        temp[x][y] = grid[i][j]
                        y += 1
                    x += 1
                if isMagicSquare(temp):
                    cnt += 1
                l += 1
                r += 1
            t += 1
            b += 1
        return cnt 
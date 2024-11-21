class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        queue = deque()
        obstacles = set()
        grid = [[0 for i in range(n)] for j in range(m)]
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        for i,j in guards:
            obstacles.add((i,j))
            queue.append((i,j))
            grid[i][j] = -1
        for i,j in walls:
            obstacles.add((i,j))
            grid[i][j] = -1
        while queue:
            i,j = queue.popleft()
            for dx,dy in dir:
                x,y = i+dx,j+dy
                while 0<=x<m and 0<=y<n:
                    if (x,y) in obstacles:
                        break
                    grid[x][y] = 1
                    x += dx
                    y += dy
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    cnt += 1
        return cnt
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque()
        zeroPos = (0,0)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==0:
                    zeroPos = (i,j)
        q.append((board,(0,0),zeroPos))
        level = 0
        req = [[1,2,3],[4,5,0]]
        vis = set()
        while q:
            size = len(q)
            for _ in range(size):
                node,prev,pos = q.popleft()
                if str(node) not in vis:
                    vis.add(str(node))
                    x,y = pos
                    if node==req:
                        return level
                    for dx,dy in dir:
                        if (dx,dy)!=prev:
                            i,j = x+dx,y+dy
                            if 0<=i<len(board) and 0<=j<len(board[0]):
                                temp = [[i for i in j] for j in node]
                                temp[i][j],temp[x][y] = temp[x][y],temp[i][j]
                                q.append((temp,(-1*dx,-1*dy),(i,j)))
            level += 1
        return -1
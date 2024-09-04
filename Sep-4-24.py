class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set()
        for ob in obstacles:
            obs.add(tuple(ob))
        dir = {
            'U':(0,1),
            'R':(1,0),
            'D':(0,-1),
            'L':(-1,0)
        }
        d = 'U'
        pos = (0,0)
        maxD = 0
        for c in commands:
            # change direction
            if c==-2:
                if d=='U': d='L'
                elif d=='L': d='D'
                elif d=='D': d='R'
                elif d=='R': d='U'
                continue
            elif c==-1:
                if d=='U': d='R'
                elif d=='R': d='D'
                elif d=='D': d='L'
                elif d=='L': d='U'
                continue
            # move
            x,y = pos
            dx,dy = dir[d]
            if dx==0:
                for i in range(1,c+1):
                    y += dy
                    if (x,y) in obs:
                        y -= dy
                        break
            else:
                for i in range(1,c+1):
                    x += dx
                    if (x,y) in obs:
                        x -= dx
                        break
            pos = (x,y)
            maxD = max(maxD,x*x+y*y)
        return maxD 



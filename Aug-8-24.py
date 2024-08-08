class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        l,r,t,b = cStart,cStart+1,rStart,rStart+1
        res = []
        vis = [[False for i in range(cols)] for j in range(rows)]
        while l>=0 or r<cols or t>=0 or b<rows:
            # l -> r
            for i in range(l,r+1):
                if 0<=t<rows and 0<=i<cols and not vis[t][i]:
                    vis[t][i] = True
                    res.append([t,i])
            l -= 1

            # t -> b
            for i in range(t,b+1):
                if 0<=i<rows and 0<=r<cols and not vis[i][r]:
                    vis[i][r] = True
                    res.append([i,r])
            t -= 1

            # r -> l
            for i in range(r,l,-1):
                if 0<=b<rows and 0<=i<cols and not vis[b][i]:
                    vis[b][i] = True
                    res.append([b,i])
            r += 1

            # b -> t
            for i in range(b,t,-1):
                if 0<=i<rows and 0<=l<cols and not vis[i][l]:
                    vis[i][l] = True
                    res.append([i,l])
            b += 1
        return res 
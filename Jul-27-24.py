class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        mat = [[float('inf') for i in range(26)] for j in range(26)]
        for i,j,c in zip(original,changed,cost):
            x,y = ord(i)-ord('a'),ord(j)-ord('a')
            mat[x][y] = min(mat[x][y],c)
        
        for via in range(len(mat)):
            for i in range(len(mat)):
                for j in range(len(mat)):
                    mat[i][j] = min(mat[i][j],mat[i][via]+mat[via][j])
        
        minCost = 0

        for s,t in zip(source,target):
            if s==t:
                continue
            x,y = ord(s)-ord('a'),ord(t)-ord('a')
            if mat[x][y]==float('inf'):
                return -1
            minCost += mat[x][y]
        
        return minCost 
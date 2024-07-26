class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        cost = [[float('inf') for i in range(n)] for j in range(n)]
        for s,d,c in edges:
            cost[s][d] = c
            cost[d][s] = c
        for i in range(n):
            cost[i][i] = 0
            
        # Floyd Warshall Algorithm
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    cost[i][j] = min(cost[i][j],cost[i][via]+cost[via][j])
        
        res,miN = -1,float('inf')
        for node,arr in enumerate(cost):
            cnt = 0
            for dist in arr:
                if dist<=distanceThreshold:
                    cnt += 1
            if cnt<miN:
                miN = cnt
                res = node
            elif cnt==miN:
                res = max(res,node)
        
        return res 
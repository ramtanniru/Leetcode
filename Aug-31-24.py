class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        maxHeap = []
        cost = defaultdict(list)
        for i in range(len(edges)):
            s,d = edges[i]
            c = succProb[i]
            cost[s].append((c,d))
            cost[d].append((c,s))
        dist = [float('-inf') for i in range(n)]
        maxHeap.append((-1,start))
        while maxHeap:
            c,node = heapq.heappop(maxHeap)
            for d,child in cost[node]:
                if dist[child]<-d*c:
                    dist[child] = -d*c
                    heapq.heappush(maxHeap,(-dist[child],child))
        return dist[end] if dist[end]!=float('-inf') else 0 
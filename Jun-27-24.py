class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vertices = len(adj.keys())
        for v,adjV in adj.items():
            if len(adjV)==vertices-1:
                return v
        return -1 
    
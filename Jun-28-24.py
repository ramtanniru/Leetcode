class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(int)
        for u,v in roads:
            d[u] += 1
            d[v] += 1
        for i in range(n):
            if i not in d:
                d[i] = 0
        l = sorted(d.items(),key= lambda x:x[1])
        cnt = 0
        i = 1
        for u,v in l:
            cnt += i*v
            i += 1
        return cnt  
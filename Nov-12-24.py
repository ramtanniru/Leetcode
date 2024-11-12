class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        maxQ = max(queries)
        cache = {}
        maxVal = 0
        items.sort()
        cache[0] = 0
        for p,q in items:
            maxVal = max(maxVal,q)
            cache[p] = maxVal
        keys = list(cache.keys())
        keys.sort()
        for q in queries:
            idx = bisect_right(keys,q)-1
            res.append(cache[keys[idx]])
        return res
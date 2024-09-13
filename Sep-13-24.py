class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [arr[0]]
        for i in arr[1:]:
            pre.append(pre[-1]^i)
        res = []
        for u,v in queries:
            if u!=0:
                res.append(pre[u-1]^pre[v])
            else:
                res.append(pre[v])
        return res 
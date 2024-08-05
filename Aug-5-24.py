class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)
        res = []
        for i in arr:
            if d[i]==1:
                res.append(i)
        if k>len(res):
            return ""
        return res[k-1] 
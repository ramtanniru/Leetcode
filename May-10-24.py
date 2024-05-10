class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res = defaultdict(list)
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                res[arr[i]/arr[j]] = [arr[i],arr[j]]
        a = sorted(res.items(),key = lambda x: x[0])
        return a[k-1][1]
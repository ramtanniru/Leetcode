class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        d = dict(Counter(arr1))
        for i in arr2:
            for j in range(d[i]):
                res.append(i)
            d.pop(i)
        for i in sorted(d.keys()):
            for j in range(d[i]):
                res.append(i)
        return res
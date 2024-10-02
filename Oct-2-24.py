class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(arr)
        hash = defaultdict(int)
        rank = 1
        res = []
        for i in sortedArr:
            if i not in hash:
                hash[i] = rank
                rank += 1
        for i in arr:
            res.append(hash[i])
        return res 
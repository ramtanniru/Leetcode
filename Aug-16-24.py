class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = float('-inf')
        maxEl,minEl = [],[]
        d = defaultdict(set)
        for i in arrays:
            maxEl.append(i[-1])
            minEl.append(i[0])
            d[i[0]].add(i[-1])
            d[i[-1]].add(i[0])
        maxEl.sort()
        minEl.sort()
        if not(minEl[0] in d[maxEl[-1]] or maxEl[-1] in d[minEl[0]]):
            return maxEl[-1]-minEl[0]
        return max(maxEl[-1]-minEl[1],maxEl[-2]-minEl[0]) 
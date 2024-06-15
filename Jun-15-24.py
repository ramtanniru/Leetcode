class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        l = [[y,x] for x,y in zip(profits,capital)]
        l.sort()
        maxHeap = []
        heapq.heapify(maxHeap)
        i = 0
        for j in range(k):
            while i<len(l) and w>=l[i][0]:
                heapq.heappush(maxHeap,-l[i][1])
                i += 1
            if not maxHeap:
                break
            w -= heapq.heappop(maxHeap)
        return w
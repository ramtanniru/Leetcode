class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        dic = dict(Counter(hand))
        minHeap = list(dic.keys())
        heapq.heapify(minHeap)
        while minHeap:
            start = minHeap[0]
            for i in range(start,start+groupSize):
                if i not in dic.keys():
                    return False
                dic[i] -= 1
                if dic[i] == 0:
                    if i!=minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
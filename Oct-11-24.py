class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chair = [i for i in range(len(times))]
        depTime = []
        arrTime = [(i,j,id) for id,(i,j) in enumerate(times)]
        heapq.heapify(arrTime)
        heapq.heapify(chair)
        c = 0
        while True:
            s,e,f = heapq.heappop(arrTime)
            while depTime and depTime[0][0]<=s:
                t,tempChair = heapq.heappop(depTime)
                heapq.heappush(chair,tempChair)
            c = heapq.heappop(chair)
            heapq.heappush(depTime,(e,c))
            if f==targetFriend:
                return c

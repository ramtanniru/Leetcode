class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        ans = ''
        if a>0:
            heapq.heappush(heap,(-a,'a'))
        if b>0:
            heapq.heappush(heap,(-b,'b'))
        if c>0:
            heapq.heappush(heap,(-c,'c'))
        while heap:
            cnt,s = heapq.heappop(heap)
            if len(ans)>=2 and ans[-1]==s and ans[-2]==s:
                if not heap:
                    break
                cnt2,s2 = heapq.heappop(heap)
                ans += s2
                cnt2 += 1
                if cnt2<0:
                    heapq.heappush(heap,(cnt2,s2))
                heapq.heappush(heap,(cnt,s))
            else:
                ans += s
                cnt += 1
                if cnt<0:
                    heapq.heappush(heap,(cnt,s))
        return ans
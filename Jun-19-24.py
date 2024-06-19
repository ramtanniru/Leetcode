class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)//k < m:
            return -1
        def isPossible(bloomDay,m,k,n):
            flowers = 0
            for b in bloomDay:
                if b<=n:
                    flowers += 1
                    if flowers==k:
                        flowers = 0
                        m -= 1
                else:
                    flowers = 0
                if m==0:
                    return True
            return m==0
        
        low,high = 0,max(bloomDay)
        while low<high:
            mid = (low+high)//2
            if isPossible(bloomDay,m,k,mid):
                high = mid
            else:
                low = mid + 1
        return low

            


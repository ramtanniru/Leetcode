class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def helper(arr):
            nonlocal cnt
            for i in range(1,len(arr)-1):
                l,r = 0,0
                for j in range(i):
                    if arr[j]<arr[i]:
                        l += 1
                for j in range(i+1,len(arr)):
                    if arr[i]<arr[j]:
                        r += 1
                if l>=1 and r>=1:
                    cnt += l*r
        cnt = 0
        helper(rating)
        helper(rating[::-1])
        return cnt  
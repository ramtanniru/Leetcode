class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis, lds = [], []
        lisArr, ldsArr = [], []
        ans = 0
        n = len(nums)
        for i in nums:
            if not lis or lis[-1]<i:
                lis.append(i)
            else:
                idx = bisect_left(lis,i)
                lis[idx] = i
            lisArr.append(len(lis))
        for i in nums[::-1]:
            if not lds or lds[-1]<i:
                lds.append(i)
            else:
                idx = bisect_left(lds,i)
                lds[idx] = i
            ldsArr.append(len(lds))
        lds = lds[::-1]
        ldsArr = ldsArr[::-1]
        for i in range(n):
            if lisArr[i]>1 and ldsArr[i]>1:
                ans = max(ans,lisArr[i]+ldsArr[i]-1)
        return n-ans
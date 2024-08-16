class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        small = arrays[0][0]
        big = arrays[0][-1]
        res = 0
        for i in range(1,len(arrays)):
            arr = arrays[i]
            res = max(res,abs(arr[-1]-small),abs(big-arr[0]))
            big = max(big,arr[-1])
            small = min(small,arr[0])
        return res 
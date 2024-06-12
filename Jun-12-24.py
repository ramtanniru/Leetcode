class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d = {0:0,1:0,2:0}
        for i in nums:
            d[i] += 1
        low = d[0]
        mid = d[1]
        high = d[2]
        for i in range(low):
            nums[i] = 0
        for i in range(low,low+mid):
            nums[i] = 1
        for i in range(low+mid,low+mid+high):
            nums[i] = 2
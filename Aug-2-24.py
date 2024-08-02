class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        windowSize = nums.count(1)
        res = float('inf')
        i,j = 1,windowSize+1
        nums += nums
        cntZero = nums[:windowSize].count(0)
        res = cntZero
        while j<=len(nums):
            if nums[i-1]==0:
                cntZero -= 1
            if nums[j-1]==0:
                cntZero += 1
            res = min(res,cntZero)
            i += 1
            j += 1
        return res 
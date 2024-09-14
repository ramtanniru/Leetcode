class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maX,streak = 0,0
        ans = 0
        i = 0
        while i<len(nums):
            if nums[i]>maX:
                maX = nums[i]
                ans = 0
                streak = 0
            if nums[i]==maX:
                streak += 1
            else:
                streak = 0
            ans = max(ans,streak)
            i += 1
        return ans 
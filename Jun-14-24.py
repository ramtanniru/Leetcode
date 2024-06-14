class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        cnt,i,j = 0,0,1
        while j<len(nums):
            if nums[j]<=nums[i]:
                cnt += nums[i]-nums[j]+1
                nums[j] = nums[i]+1
            i += 1
            j += 1
        return cnt
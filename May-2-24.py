class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        while abs(nums[i])!=nums[j] and i<j:
            if abs(nums[i])>nums[j]:
                i += 1
            else:
                j -= 1
        if i>=j or abs(nums[i])!=nums[j] or nums[i]==nums[j]:
            return -1
        return nums[j]
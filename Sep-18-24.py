class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums)==1: return str(nums[0])
        nums = [str(i) for i in nums]
        nums.sort(key=lambda x:x*10,reverse=True)
        if nums[0]=='0': return '0'
        return "".join(nums) 
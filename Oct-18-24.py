class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def bt(i=0,val=0):
            nonlocal maX,ans
            if val==maX:
                ans += 1
            for i in range(i,len(nums)):
                bt(i+1,val|nums[i])
        maX = 0
        ans =0
        for i in nums:
            maX |= i
        bt()
        return ans
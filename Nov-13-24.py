class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def countPairsSum(val):
            l,r = 0,len(nums)-1
            res = 0
            while l<r:
                while l<r and nums[l]+nums[r]>val:
                    r -= 1
                res += r-l
                l += 1
            return res
        ans = 0
        nums.sort()
        return countPairsSum(upper) - countPairsSum(lower-1)
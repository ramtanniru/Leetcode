class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits = {}
        ans = inf
        for i,x in enumerate(nums):
            bits = {_or | x : left for _or,left in bits.items()}
            bits[x] = i
            for _or,left in bits.items():
                if _or >= k:
                    ans = min(ans,i-left+1)
        return ans if ans!=inf else -1
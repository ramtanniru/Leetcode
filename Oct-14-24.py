class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        sc = 0
        while k>0:
            ele = -heapq.heappop(nums)
            sc += ele
            heapq.heappush(nums,-math.ceil(ele/3))
            k -= 1
        return sc
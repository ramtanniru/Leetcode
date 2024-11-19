class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cache = defaultdict(int)
        ans = 0
        size = 0
        s = 0
        for i in range(k):
            cache[nums[i]] += 1
        size = len(cache)
        for key,v in cache.items():
            s += key*v
        if size==k:
            ans = max(ans,s)
        for i in range(k,len(nums)):
            if cache[nums[i-k]]==1:
                size -= 1
                del cache[nums[i-k]]
            else:
                cache[nums[i-k]] -= 1
            if nums[i] not in cache:
                size += 1
            cache[nums[i]] += 1
            s -= nums[i-k]
            s += nums[i]
            if size==k:
                ans = max(ans,s)
        return ans
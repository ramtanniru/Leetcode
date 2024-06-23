class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # TLE
        # maxLen = 1
        # i = 1
        # while i<lem(nums)-1:
        #     j = i+1
        #     mi = nums[i]
        #     ma = nums[i]
        #     while j<len(nums):
        #         mi = min(mi,nums[j])
        #         ma = max(ma,nums[j])
        #         if abs(mi-ma)<=limit:
        #             maxLen = max(maxLen,j-i+1)
        #         else:
        #             i = j-1
        #             break
        #         j += 1
        #     i += 1
        # return maxLen 

        minQ = deque()
        maxQ = deque()
        maxLen = 0
        l = 0
        for r in range(len(nums)):
            while minQ and nums[r] < minQ[-1]:
                minQ.pop()
            while maxQ and nums[r] > maxQ[-1]:
                maxQ.pop()
            minQ.append(nums[r])
            maxQ.append(nums[r])

            while maxQ[0] - minQ[0] > limit:
                if nums[l] == maxQ[0]:
                    maxQ.popleft()
                if nums[l] == minQ[0]:
                    minQ.popleft()
                l += 1
            maxLen = max(maxLen,r - l + 1)
        return maxLen 
        
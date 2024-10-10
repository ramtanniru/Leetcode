class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        forward = []
        backward = []
        for i in nums:
            if not forward:
                forward.append(i)
            elif forward[-1]>i:
                forward.append(i)
            else:
                forward.append(forward[-1])
        for i in nums[::-1]:
            if not backward:
                backward.append(i)
            elif backward[-1]<i:
                backward.append(i)
            else:
                backward.append(backward[-1])
        backward = backward[::-1]
        i,j = 0,0
        maX = 0
        while i<len(nums) and j<len(nums):
            while i<len(nums) and j<len(nums) and forward[i]<=backward[j]:
                maX = max(maX,j-i)
                j += 1
            i += 1
        return maX 

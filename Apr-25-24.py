class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*27
        n = 27
        for i in s:
            idx = ord(i)-ord('a')
            maximum = float('-inf')

            leftRange = max((idx-k),0)
            rightRange = min((idx+k),26)

            for j in range(leftRange,rightRange+1):
                maximum = max(maximum,dp[j])
            dp[idx] = maximum + 1
        return max(dp)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        def rec(idx=0,b=0):
            if idx>=len(s):
                return 0
            if dp[idx][b]!=-1:
                return dp[idx][b]
            if b:
                if s[idx]=='a':
                    res = 1 + rec(idx+1,b)
                else:
                    res = rec(idx+1,b)
            else:
                if s[idx]=='b':
                    res = min(1+rec(idx+1,b),rec(idx+1,1))
                else:
                    res = rec(idx+1,b)
            dp[idx][b] = res
            return dp[idx][b] 
        dp = [[-1,-1] for i in range(len(s)+1)]
        return rec() 

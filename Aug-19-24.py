class Solution:
    def minSteps(self, n: int) -> int:
        def rec(l,c):
            if l>n:
                return float('inf')
            if l==n:
                return 0
            if (l,c) in dp:
                return dp[(l,c)]
            copyAll = 2 + rec(l+l,l)
            paste = 1 + rec(l+c,c)
            dp[(l,c)] = min(copyAll,paste)
            return dp[(l,c)]
        if n==1:
            return 0
        dp = defaultdict()
        return 1 + rec(1,1) 
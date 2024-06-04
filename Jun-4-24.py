class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = dict(Counter(s))
        cnt,odd = 0,0
        l = sorted(d.values(),reverse = True)
        for i in l:
            if i%2==0:
                cnt += i
            else:
                odd += 1
                cnt += i-1
        if odd!=0:
            return cnt+1
        return cnt
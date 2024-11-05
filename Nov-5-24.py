class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        i,j = 0,1
        while j<len(s):
            if s[i]!=s[j]:
                ans += 1
            i+=2
            j+=2
        return ans
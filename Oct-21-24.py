class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def bt(i=0,seen=set()):
            if i==len(s):
                return 0
            ans = 0
            for j in range(i+1,len(s)+1):
                if s[i:j] not in seen:
                    seen.add(s[i:j])
                    ans = max(ans,1+bt(j,seen))
                    seen.remove(s[i:j])
            return ans
        return bt()
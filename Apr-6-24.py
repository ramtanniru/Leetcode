class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l,r = 0,0
        flag = 0
        res = ""

        for i in s:
            if i=="(":
                l+=1
                flag+=1
            elif i==")" and flag>0:
                r+=1
                flag-=1
        l,r = min(l,r),min(l,r)
        for i in s:
            if i=='(':
                if l>0:
                    res+=i
                    l-=1
            elif i==')':
                if r>0 and r>l:
                    res+=i
                    r-=1
            else:
                res+=i
        return res
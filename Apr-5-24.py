class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        if(len(s)==1):
            return s
        stk.append(s[0])
        for i in range(1,len(s)):
            if(len(stk)!=0 and (abs(ord(stk[-1])-ord(s[i]))==32)):
                stk.pop(-1)
            else:
                stk.append(s[i])
        s = ""
        for i in stk:
            s+=i
        return s

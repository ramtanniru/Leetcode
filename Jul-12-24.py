class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def findMax(s,x,y,s1,s2):
            sc = 0
            stk = []
            for i in s:
                if stk and stk[-1]==s1[0] and i==s1[1]:
                    sc += x
                    stk.pop()
                else:
                    stk.append(i)
            s = "".join(stk)
            stk = []
            for i in s:
                if stk and stk[-1]==s2[0] and i==s2[1]:
                    sc += y
                    stk.pop()
                else:
                    stk.append(i)
            return sc
        if x>y:
            return findMax(s,x,y,"ab","ba")
        else:
            return findMax(s,y,x,"ba","ab") 
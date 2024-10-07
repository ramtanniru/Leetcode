class Solution:
    def minLength(self, s: str) -> int:
        stk = []
        for i in s:
            if not stk:
                stk.append(i)
            else:
                stk.append(i)
                while len(stk)>=2 and stk[-2]+stk[-1] in ['AB','CD']:
                    stk.pop()
                    stk.pop()
        return len(stk) 
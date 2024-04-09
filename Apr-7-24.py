class Solution:
    def checkValidString(self, s: str) -> bool:
        lMin,lMax = 0,0
        for i in s:
            if i=='(':
                lMax,lMin = lMax+1, lMin+1
            elif i==')':
                lMax,lMin = lMax-1, lMin-1
            else:
                lMax,lMin = lMax+1, lMin-1
            if lMax<0:
                return False
            if lMin<0:
                lMin = 0
        return lMin==0
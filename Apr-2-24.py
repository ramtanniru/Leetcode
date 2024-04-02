class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mS,mT = {},{}
        for a,b in zip(s,t):
            if((a in mS and mS[a]!=b) or (b in mT and mT[b]!=a)):
                return False
            mS[a] = b
            mT[b] = a
        return True

'''
Method-2
Using sets
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        setS = len(set(s))
        setT = len(set(t))
        setST = len(set(zip(s,t)))
        return setS==setT==setST
'''
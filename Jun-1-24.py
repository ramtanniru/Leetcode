class Solution:
    def scoreOfString(self, s: str) -> int:
        l = [ord(i) for i in s]
        Sum,i = 0,0
        while i<len(s)-1:
            Sum += abs(l[i]-l[i+1])
            i += 1
        return Sum
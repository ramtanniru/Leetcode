class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ug = [1]
        x,y,z = 0,0,0
        while len(ug)<n:
            least = min(ug[x]*2,ug[y]*3,ug[z]*5)
            if least not in ug:
                ug.append(least)
            if least == ug[x]*2:
                x+=1
            elif least == ug[y]*3:
                y+=1
            elif least == ug[z]*5:
                z+=1
        return ug[-1] 
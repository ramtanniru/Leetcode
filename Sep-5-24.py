class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        t = mean*(len(rolls)+n)-sum(rolls)
        res = []
        if t<n or t>n*6: return res
        avg = t//n
        offset = t%n
        for i in range(n):
            res.append(avg)
            if offset>0:
                res[-1] += 1
            offset -= 1
        return res 
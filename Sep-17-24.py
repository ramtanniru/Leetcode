class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1+" "+s2
        li = s.split(' ')
        c = Counter(li)
        res = []
        for k,v in c.items():
            if v==1:
                res.append(k)
        return res 
class Solution:
    def minimumPushes(self, word: str) -> int:
        d = Counter(word)
        li = sorted(list(d.values()),reverse=True)
        inc,res = 1,0
        i = 0
        print(li)
        while i<len(li):
            for _ in range(8):
                if i==len(li):
                    break
                res += li[i]*inc
                i += 1
            inc += 1
        return res 
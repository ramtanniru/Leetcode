class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        li = []
        for i in words:
            li.append(Counter(i))
        for i in words[0]:
            chk = 0
            for j in li[1:]:
                if j[i]==0:
                    chk += 1
            if chk==0:
                for j in li[1:]:
                    j[i] -= 1
                res.append(i)
        return res
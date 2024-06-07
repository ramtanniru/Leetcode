class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = []
        s = set(dictionary)
        for i in sentence.split():
            for j in range(len(i)):
                if i[:j] in s:
                    res.append(i[:j])
                    break
            if j==len(i)-1 and i[:j] not in s:
                res.append(i)
        return " ".join(res)
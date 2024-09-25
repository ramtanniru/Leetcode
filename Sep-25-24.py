class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        d = defaultdict(int)
        for i in range(len(words)):
            for j in range(1,len(words[i])+1):
                d[words[i][:j]] += 1
        res = [0 for i in range(len(words))]
        for i in range(len(words)):
            for j in range(1,len(words[i])+1):
                res[i] += d[words[i][:j]]
        return res 

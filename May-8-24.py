class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = {}
        newScores = sorted(score,reverse=True)
        for i,x in enumerate(newScores):
            if i==0:
                ranks[x] = "Gold Medal"
            elif i==1:
                ranks[x] = "Silver Medal"
            elif i==2:
                ranks[x] = "Bronze Medal"
            else:
                ranks[x] = str(i+1)
        res = []
        for i in score:
            res.append(ranks[i])
        return res
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        s,d = 0,0
        happiness.sort()
        n = len(happiness)
        k = min(n,k)
        for i in range(1,k+1):
            val = happiness[n-i]
            if val>0 and val-d>=0:
                s += val-d
            d += 1
        return s
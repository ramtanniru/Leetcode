class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        cnt = 0
        for i,x in enumerate(heights):
            if x!=exp[i]:
                cnt += 1
        return cnt
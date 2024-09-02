class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        i = 0
        while i<len(chalk):
            if chalk[i]>k:
                break
            k -= chalk[i]
            i += 1
        return i 
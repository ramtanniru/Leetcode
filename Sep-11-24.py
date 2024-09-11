class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = bin(start^goal)
        return res.count('1') 
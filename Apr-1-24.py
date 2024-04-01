class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = [i for i in s.split()]
        return len(a[-1])
class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt = 0
        ones = 0
        for i in s:
            if i=='0': cnt += ones
            else: ones += 1
        return cnt
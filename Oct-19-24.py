class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(s):
            return s[::-1]
        def invert(s):
            return "".join(['0' if i=='1' else '1' for i in s])
        a = "0"
        for i in range(n):
            b = a+"1"+reverse(invert(a))
            a = b
        return a[k-1]
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time<n:
            i = 1
            for _ in range(time):
                i += 1
            return i

        if (time//(n-1))%2!=0:
            i = n
            for _ in range(time%(n-1)):
                i -= 1
        else:
            i = 1
            for _ in range(time%(n-1)):
                i += 1
        return i 
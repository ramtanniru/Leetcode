class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def jos(n,k):
            if n==1:
                return 1
            return (jos(n-1,k)+k-1)%n+1
        return jos(n,k) 
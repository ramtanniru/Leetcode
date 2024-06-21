class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], m: int) -> int:
        initSat = 0
        n = len(customers)
        for i in range(n):
            if grumpy[i]!=1:
                initSat += customers[i]
        i,j = 0,m
        extraSat = []
        while j<=n:
            cust = 0
            for x in range(i,j):
                if grumpy[x]==1:
                    cust += customers[x]
            extraSat.append(cust)
            i += 1
            j += 1
        return initSat+max(extraSat)  
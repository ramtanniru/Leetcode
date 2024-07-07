class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def rec(dr=0,c=0,b=numBottles):
            if b+c<numExchange:
                return dr+b
            dr += b
            x = (b+c)//numExchange
            c = (b+c)%numExchange
            return rec(dr,c,x)
        return rec() 
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        i = 0
        wt = 0
        t = customers[0][0] 
        while i<len(customers):
            st = customers[i][0]
            t = t+customers[i][1] if t>customers[i][0] else st+customers[i][1]
            wt += t-st
            i += 1
        return wt/len(customers) 
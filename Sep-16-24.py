class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minTime = float('inf')
        temp = []
        for i in timePoints:
            aH,aM = map(int,i.split(':'))
            temp.append(aH*60+aM)
        temp.sort()
        for i in range(len(temp)):
            a,b = temp[i-1],temp[i]
            minTime = min(minTime,min(abs(b-a)%1440,(1440-abs(b-a))%1440))
        return minTime 
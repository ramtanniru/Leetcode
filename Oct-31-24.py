class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        def rec(i=0,j=0,limit=0):
            nonlocal robot,factory
            if i>=len(robot):
                return 0
            if j>=len(factory):
                return float('inf')
            
            if (i,j,limit) in dp:
                return dp[(i,j,limit)]

            notTake = rec(i,j+1,0)

            take = float('inf')
            if factory[j][1]>limit:
                dist = abs(factory[j][0]-robot[i])
                take = dist + rec(i+1,j,limit+1)
            
            dp[(i,j,limit)] = min(take,notTake)
            return dp[(i,j,limit)]
        
        robot.sort()
        factory.sort()
        dp = defaultdict(int)
        return rec()
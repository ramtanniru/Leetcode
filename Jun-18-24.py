class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [(x,y) for x,y in zip(difficulty,profit)]
        sorted_jobs = sorted(jobs,key=lambda x:x[1],reverse=True)
        worker.sort()
        res, = 0
        for w in worker:
            for i,j in sorted_jobs:
                if i<=w:
                    res += j
                    break
        return res
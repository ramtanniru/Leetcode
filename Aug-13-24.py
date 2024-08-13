class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def rec(idx,s,comb=[]):
            if s == target:
                curr = tuple(comb)
                if curr not in ans:
                    ans.add(curr)
                    res.append(curr)
                return
            if idx==len(candidates):
                return
            if s+candidates[idx]<=target:
                take = rec(idx+1,s+candidates[idx],comb+[candidates[idx]])
            while idx<len(candidates)-1 and candidates[idx+1]==candidates[idx]:
                idx += 1
            notTake = rec(idx+1,s,comb)
        ans = set()
        res = []
        candidates.sort()
        rec(0,0)
        return res 
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        res = []
        flag = 0
        for i in nums[:k]:
            if not q or i-q[-1]==1:
                flag -= 1
                q.append(i)
            else:
                flag = k-1
                q.append(i)
        if flag>0:
            res.append(-1)
        else:
            res.append(q[-1])
        for i in nums[k:]:
            if i-q[-1]!=1:
                flag = k-1
                q.append(i)
            else:
                flag -= 1
                q.append(i)
            if flag>0:
                res.append(-1)
            else:
                res.append(q[-1])
            q.popleft()
        return res
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        for i in logs:
            if i=='./':
                continue
            elif i=='../':
                if stk:
                    stk.pop()
            else:
                stk.append(i[:-1])
        return len(stk) 
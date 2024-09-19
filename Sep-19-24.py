class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        if not expression:
            return []
        if len(expression)==1:
            return [int(expression)]
        if len(expression)==2 and expression[0].isdigit():
            return [int(expression)]
        for i,op in enumerate(expression):
            if op.isdigit():
                continue
            leftRes = self.diffWaysToCompute(expression[:i])
            rightRes = self.diffWaysToCompute(expression[i+1:])

            for l in leftRes:
                for r in rightRes:
                    if op=='+':
                        res.append(l+r)
                    elif op=='-':
                        res.append(l-r)
                    elif op=='*':
                        res.append(l*r)
        return res 
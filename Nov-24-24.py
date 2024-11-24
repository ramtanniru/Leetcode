class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        miN = float('inf')
        neg = 0
        s = 0
        for row in matrix:
            for ele in row:
                miN = min(miN,abs(ele))
                if ele<0:
                    neg += 1
                s += abs(ele)
        return s if neg%2==0 else s-(2*miN)
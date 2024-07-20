class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        mat = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]
        i,j = 0,0
        while i<len(rowSum) and j<len(colSum):
            x = min(rowSum[i],colSum[j])
            mat[i][j] = x
            rowSum[i] -= x
            colSum[j] -= x
            if rowSum[i]==0:
                i += 1
            if colSum[j]==0:
                j += 1
        return mat 
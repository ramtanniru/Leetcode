class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        mat = [[0 for i in range(n)] for j in range(m)]
        if m*n!=len(original):
            return []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = original[i*n+j]
        return mat 
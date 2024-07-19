class Solution:
    def __init__(self):
        self.rows = defaultdict(list)
        self.cols = defaultdict(list)
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        def minRow(arr):
            miN,idx = float('inf'),-1
            for i,x in enumerate(arr):
                if miN>x:
                    miN = x
                    idx = i
            return (miN,idx)
        def maxCol(mat,col):
            i = 0
            maX,idx = float('-inf'),-1
            while i<len(mat):
                if maX<mat[i][col]:
                    maX = mat[i][col]
                    idx = col
                i += 1
            return (maX,idx)
        for row in mat:
            val,idx = minRow(row)
            self.rows[idx].append(val)
        for i in range(len(mat[0])):
            val,idx = maxCol(mat,i)
            self.cols[idx].append(val)
        res = []
        for i in range(max(len(mat),len(mat[0]))):
            rowSet = set()
            for j in self.rows[i]:
                rowSet.add(j)
            for j in self.cols[i]:
                if j in rowSet:
                    res.append(j)                
        return res 

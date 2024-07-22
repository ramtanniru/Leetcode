class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = []
        for i,j in zip(names,heights):
            l.append([i,j])
        l = sorted(l,key=lambda x:x[1],reverse=True)
        res = []
        for i in l:
            res.append(i[0])
        return res 
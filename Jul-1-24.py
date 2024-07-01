class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        i,j,k = 0,1,2
        while k<len(arr):
            if (arr[i]%2)*(arr[j]%2)*(arr[k]%2)!=0:
                return True
            i += 1
            j += 1
            k += 1
        return False 
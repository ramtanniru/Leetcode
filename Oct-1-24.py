class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if sum(arr)%k!=0: return False
        rem = [0]*k
        for i in arr:
            rem[i%k] += 1
        for i in range(1,(k//2)+1):
            if rem[i]!=rem[k-i]: return False
        return True 
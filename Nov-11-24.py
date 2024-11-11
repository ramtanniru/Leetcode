class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def sieve(n):
            s = []
            vis = [True for _ in range(n)]
            for i in range(2,int(n**0.5)+1):
                if vis[i]:
                    for j in range(i*i,n,i):
                        vis[j] = False
            for i in range(2,n):
                if vis[i]:
                    s.append(i)
            return s
        i = len(nums)-2
        prime = sieve(max(nums))
        while i>=0:
            if nums[i]>=nums[i+1]:
                temp = nums[i]
                j = 0
                while temp>=nums[i+1] and j<len(prime) and prime[j]<temp:
                    if temp - prime[j] < nums[i+1]:
                        nums[i] = temp-prime[j]
                        break
                    j += 1
                if nums[i] >= nums[i+1]:
                    return False
            i -= 1
        return True
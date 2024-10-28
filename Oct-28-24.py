class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        rootMap = defaultdict(int)
        ansMap = defaultdict(int)
        s = set(nums)
        nums = list(set(nums))
        nums.sort()
        for i in nums:
            if i*i in s:
                if i in rootMap:
                    rootMap[i*i] = rootMap[i]
                else:
                    rootMap[i*i] = i
                ansMap[rootMap[i*i]] += 1
        if not ansMap: return -1
        return max(list(ansMap.values()))+1
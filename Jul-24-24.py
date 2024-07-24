class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for num in nums:
            val = ""
            for i in str(num):
                val += str(mapping[int(i)])
            d[int(val)].append(num)
        l = sorted(d.items(),key = lambda x:x[0])
        res = []
        for item in l:
            res+=item[1]
        return res 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        a = Counter(nums1)
        b = Counter(nums2)
        if len(a.keys())>len(b.keys()):
            for i in b.keys():
                for j in range(min(a[i],b[i])):
                    res.append(i)
        else:
            for i in a.keys():
                for j in range(min(a[i],b[i])):
                    res.append(i)
        return res 

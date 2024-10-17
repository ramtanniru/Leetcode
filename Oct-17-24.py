class Solution:
    def maximumSwap(self, num: int) -> int:
        map = defaultdict(int)
        l = list(str(num))
        for i,x in enumerate(l):
            map[int(x)] = i
        for i,x in enumerate(l):
            for j in range(9,int(x),-1):
                if j in map:
                    if map[j]>i:
                        l[i],l[map[j]] = l[map[j]],l[i]
                        return int(''.join(l))
        return num
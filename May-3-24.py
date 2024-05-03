class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = 0
        v1 = list(map(int,version1.split('.')))
        v2 = list(map(int,version2.split('.')))
        if v1==v2:
            return 0
        while i<len(v1) and i<len(v2):
            if v1[i]==v2[i]:
                i += 1
            else:
                if v1[i]>v2[i]:
                    return 1
                return -1
        while i<len(v1):
            if v1[i]>0:
                return 1
            i += 1
        while i<len(v2):
            if v2[i]>0:
                return -1
            i += 1
        return 0
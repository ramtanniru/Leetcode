class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for w in words:
            flag = True
            for ch in w:
                if ch not in allowed:
                    flag = False
                    break
            if flag: res += 1
        return res 
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r = 0,len(skill)-1
        chem = 0
        t = skill[0] + skill[-1]
        while l<r:
            if skill[l] + skill[r] != t:
                return -1
            chem += skill[l]*skill[r]
            l += 1
            r -= 1
        return chem 
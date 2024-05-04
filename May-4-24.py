class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats,l,r = 0,0,len(people)-1
        people.sort()
        while l<r:
            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            elif people[l] + people[r] > limit:
                if people[r] <= limit:
                    r -= 1
                    boats += 1
        if l==r:
            boats += 1
        return boats
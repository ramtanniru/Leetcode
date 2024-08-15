class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        purse = { 5 : 0, 10 : 0, 20 : 0 }

        for i in bills:
            if i==10:
                if purse[5]==0:
                    return False
                purse[5] -= 1
            if i==20:
                if purse[10]>0 and purse[5]>0:
                    purse[10] -= 1
                    purse[5] -= 1
                elif purse[5]>2:
                    purse[5] -= 3
                else:
                    return False
            purse[i] += 1
        return True 
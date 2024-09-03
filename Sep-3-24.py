class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = ""
        for i in s:
            temp += str(ord(i)-ord('a')+1)
        for _ in range(k):
            curr = 0
            print(temp)
            for i in temp:
                curr += int(i)
            temp = str(curr)
        return int(temp) 
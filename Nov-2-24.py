class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l = sentence.split(" ")
        first_char = l[0][0]
        last_char = l[0][-1]
        i = 1
        while i<len(l):
            f_char = l[i][0]
            if f_char!=last_char:
                return False
            last_char = l[i][-1]
            i += 1
        return first_char==last_char
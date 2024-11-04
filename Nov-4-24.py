class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        freq = 1
        for i in range(1,len(word)):
            if freq==9 or word[i]!=word[i-1]:
                comp += str(freq)+word[i-1]
                freq = 1
            else:
                freq += 1
        comp += str(freq)+word[-1]
        return comp
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        a = word[0]
        i = 1
        while i<len(word) and word[i-1]!=ch:
            a += word[i]
            i += 1
        return a[::-1]+word[i:]
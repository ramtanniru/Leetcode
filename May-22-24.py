class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s==s[::-1]
        def bt(start=0,path=[]):
            if start==len(s):
                res.append(path)
                return
            for i in range(start+1,len(s)+1):
                if isPalindrome(s[start:i]):
                    bt(i,path+[s[start:i]])
        res = []
        bt()
        return res
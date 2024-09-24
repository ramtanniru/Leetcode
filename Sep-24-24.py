class TrieNode:
    def __init__(self):
        self.map = defaultdict(TrieNode)
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.map:
                curr.map[c] = TrieNode()
            curr = curr.map[c]
        curr.isEnd = True
    def prefixLen(self,word):
        curr = self.root
        l = 0
        for c in word:
            if c not in curr.map:
                return l
            l += 1
            curr = curr.map[c]
        return l
            
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Trie approach
        # res = 0
        # for i in arr2:
        #     currTrie = Trie()
        #     currTrie.insert(str(i))
        #     for j in arr1:
        #         res = max(res,currTrie.prefixLen(str(j)))
        # return res
        res = 0
        s = set()
        for _i in arr1:
            i = str(_i)
            for j in range(len(i)+1):
                s.add(i[:j])
        for _i in arr2:
            i = str(_i)
            for j in range(len(i)+1):
                if i[:j] in s:
                    res = max(res,j)
        return res 
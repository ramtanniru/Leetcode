class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        res = [-1]*n
        pos = deque(range(n))
        for i in deck:
            index = pos.popleft()
            res[index] = i
            if pos:
                pos.append(pos.popleft())
        return res
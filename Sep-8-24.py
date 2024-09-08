class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def findLen(root):
            if not root: return 0
            return 1 + findLen(root.next)
        Len = findLen(head)
        offset = Len%k
        size = Len//k
        curr = head
        res = []
        while curr:
            i = size-1
            if offset>0:
                i += 1
                offset -= 1
            h = ListNode(curr.val)
            curr = curr.next
            li = h
            while curr and i>0:
                li.next = ListNode(curr.val)
                li = li.next
                curr = curr.next
                i -= 1
            res.append(h)
        while len(res)<k:
            res.append(None)
        return res 
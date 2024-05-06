class Solution:
    # TLE
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev,curr = dummy,head
        while curr:
            temp = curr.next
            while temp:
                if temp.val>curr.val:
                    prev.next = curr.next
                    break
                temp = temp.next
            if not temp:
                prev = curr
            curr = curr.next
        return dummy.next
    # Using stack
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        curr = head
        while curr:
            if stk:
                while stk and stk[-1]<curr.val:
                    stk.pop()
                stk.append(curr.val)
            else:
                stk.append(curr.val)
            curr = curr.next
        i = 1
        if not stk:
            return
        head = ListNode(stk[0])
        curr = head
        while i<len(stk):
            curr.next = ListNode(stk[i])
            curr = curr.next
            i += 1
        return head
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode(0)
        temp = l
        flag = False
        curr = head
        s = 0
        while curr:
            if curr.val == 0 and s!=0:
                flag = True
            if flag:
                temp.next = ListNode(s)
                temp = temp.next
                s = 0
                flag = False
            else:
                s += curr.val
            curr = curr.next 
        return l.next 
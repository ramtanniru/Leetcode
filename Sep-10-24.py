class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        curr = head
        while curr and curr.next:
            a = curr.val
            b = curr.next.val
            temp = curr.next
            curr.next = ListNode(gcd(a,b),temp)
            curr = temp
        return head 
class Solution:
    def __init__(self):
        self.carry = 0
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        def double(node):
            if node.next:
                double(node.next)
            x = 2*node.val
            node.val = x%10 + self.carry
            self.carry = x//10
        double(curr)
        if self.carry!=0:
            dummy = ListNode(self.carry)
            dummy.next = head
            return dummy
        return head
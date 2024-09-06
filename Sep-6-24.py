class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        def deleteNode(node):
            if not node.next.next:
                node.next = None
                return node
            node.next = node.next.next
            return node
        nums = set(nums)
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while curr and curr.next:
            if curr.next.val in nums:
                curr = deleteNode(curr)
            else:
                curr = curr.next
        return dummy.next 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        l,r,t,b = 0,n-1,0,m-1
        mat = [[-1 for i in range(n)] for j in range(m)]
        curr = head
        while l<=r and t<=b:
            # l --> r
            for i in range(l,r+1):
                if curr:
                    mat[t][i] = curr.val
                    curr = curr.next
            t += 1

            # t --> b
            for i in range(t,b+1):
                if curr:
                    mat[i][r] = curr.val
                    curr = curr.next
            r -= 1

            # r --> l
            for i in range(r,l-1,-1):
                if curr:
                    mat[b][i] = curr.val
                    curr = curr.next
            b -= 1

            # b --> t
            for i in range(b,t-1,-1):
                if curr:
                    mat[i][l] = curr.val
                    curr = curr.next
            l += 1
        return mat 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [float('inf'),float('-inf')]
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        arr = []
        if n>=4:
            back,curr,front = head,head.next,head.next.next
            i = 1
            while front:
                if back.val<curr.val>front.val or back.val>curr.val<front.val:
                    arr.append(i)
                back = curr
                curr = front
                front = front.next
                i += 1
            if len(arr)<2:
                return [-1,-1]
            l,r = 0,1
            maX,miN = arr[0],arr[0]
            minLocal = arr[r]-arr[l]
            print(arr)
            while r<len(arr):
                minLocal = min(minLocal,arr[r]-arr[l])
                maX,miN = max(maX,arr[r]),min(miN,arr[r])
                l += 1
                r += 1
            res[0] = minLocal
            res[1] = maX-miN
            return res
        return [-1,-1] 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inOrd(root,res = []):
            if not root:
                return res
            inOrd(root.left,res)
            res.append(root.val)
            inOrd(root.right,res)
            return res
        arr = inOrd(root)
        def build(arr):
            if not arr:
                return
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid+1:]
            root = TreeNode(arr[mid])
            root.left = build(left)
            root.right = build(right)
            return root
        return build(arr) 
    
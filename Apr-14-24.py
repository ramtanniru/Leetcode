class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = 0
        if root.left!=None:
            if root.left.left==None and root.left.right==None:
                s+=root.left.val
            s+=self.sumOfLeftLeaves(root.left)
        if root.right!=None:
            s+=self.sumOfLeftLeaves(root.right)
        if root.left==None:
            return s
        return s
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            curr = TreeNode(val)
            curr.left = root
            return curr
        def preOrder(root,d,depth,val):
            if root:
                d += 1
                if d==depth:
                    print(root.val)
                    tempLeft = root.left
                    tempRight = root.right
                    if root.left!=None:
                        l = TreeNode(val)
                        root.left = l
                        l.left = tempLeft
                    else:
                        root.left = TreeNode(val)
                    if root.right!=None:
                        r = TreeNode(val)
                        root.right = r
                        r.right = tempRight
                    else:
                        root.right = TreeNode(val)
                    return
                if root.left:
                    preOrder(root.left,d,depth,val)
                if root.right:
                    preOrder(root.right,d,depth,val)
            return
        preOrder(root,1,depth,val)
        return root
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post(root):
            if not root:
                return
            post(root.left)
            post(root.right)
            res.append(root.val)
        res = []
        post(root)
        return res 
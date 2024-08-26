class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def post(root):
            if not root:
                return
            for c in root.children:
                post(c)
            res.append(root.val)
        res = []
        post(root)
        return res 
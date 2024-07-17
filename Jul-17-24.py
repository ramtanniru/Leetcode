class Solution:
    def __init__(self):
        self.res = []
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(root,s,flag = True):
            if not root:
                return
            if flag and root.val not in s:
                self.res.append(root)
                flag = False
            if root.left and root.left.val in s:
                temp = root.left
                root.left = None
                dfs(temp,s,True)
            else:
                dfs(root.left,s,flag)
            if root.right and root.right.val in s:
                temp = root.right
                root.right = None
                dfs(temp,s,True) 
            else:
                dfs(root.right,s,flag) 
        dfs(root,set(to_delete))
        return self.res 
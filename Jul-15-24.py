# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = defaultdict(dict)
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        def buildTree(root):
            if 'l' in self.d[root.val]:
                root.left = buildTree(TreeNode(self.d[root.val]['l']))
            if 'r' in self.d[root.val]:
                root.right = buildTree(TreeNode(self.d[root.val]['r']))
            return root

        # parent->child mapping
        for i in descriptions:
            if i[2]==1:
                self.d[i[0]]['l'] = i[1]
            else:
                self.d[i[0]]['r'] = i[1]

        # fiding root
        parents = set()
        for i in descriptions:
            parents.add(i[0])
        for i in descriptions:
            if i[1] in parents:
                parents.remove(i[1])
        for i in parents:
            p = i

        # building B-tree
        root = buildTree(TreeNode(p))
        
        return root 
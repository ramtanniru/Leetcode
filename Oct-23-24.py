class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([])
        parentHash = defaultdict(TreeNode)
        sumHash = defaultdict(int)
        q.append(root)
        parentHash[id(root)] = TreeNode(0)
        while q:
            numOfChildren = len(q)
            levelSum = 0
            tempq = deque([])
            for child in range(numOfChildren):
                node = q.popleft()
                tempq.append(node)
                levelSum += node.val
                nodeChildSum = 0
                if node.left:
                    parentHash[id(node.left)] = node
                    q.append(node.left)
                    nodeChildSum += node.left.val
                if node.right:
                    parentHash[id(node.right)] = node
                    q.append(node.right)
                    nodeChildSum += node.right.val
                sumHash[id(node)] = nodeChildSum
            while tempq:
                node = tempq.popleft()
                node.val = levelSum - sumHash[id(parentHash[id(node)])]
        root.val = 0
        return root
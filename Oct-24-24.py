class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        childMap1 = defaultdict(set)
        childMap2 = defaultdict(set)
        q1 = deque()
        q2 = deque()
        q1.append(root1)
        q2.append(root2)
        while q1 and q2:
            n1,n2 = q1.popleft(),q2.popleft()
            child1,child2 = set(),set()
            if n1.left:
                child1.add(n1.left.val)
                q1.append(n1.left)
            if n1.right:
                child1.add(n1.right.val)
                q1.append(n1.right)
            if n2.left:
                child2.add(n2.left.val)
                q2.append(n2.left)
            if n2.right:
                child2.add(n2.right.val)
                q2.append(n2.right)
            childMap1[n1.val] = child1
            childMap2[n2.val] = child2
        if q1 or q2 or childMap1.keys()!=childMap2.keys():
            return False
        for k in childMap1.keys():
            if childMap1[k]!=childMap2[k]:
                return False
        return True
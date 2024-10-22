class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def depth(root):
            if not root:
                return 0
            return 1+max(depth(root.left),depth(root.right))
        def dfs(root,l):
            nonlocal levels
            if not root:
                return
            levels[l].append(root.val)
            dfs(root.left,l+1)
            dfs(root.right,l+1)
        heap = []
        height = depth(root)
        if height<k: return -1
        levels = [[] for i in range(height)]
        dfs(root,0)
        for l in levels[:k]:
            heapq.heappush(heap,sum(l))
        for l in levels[k:]:
            s = sum(l)
            if heap[0]<s:
                heapq.heappop(heap)
                heapq.heappush(heap,s)
        return heap[0]
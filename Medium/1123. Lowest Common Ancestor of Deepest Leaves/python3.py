class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = None
        self.maxDepth = -1

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        return self.res

    def dfs(self, node: TreeNode, depth: int) -> int:
        if node is None:
            self.maxDepth = max(self.maxDepth, depth)
            return depth

        left = self.dfs(node.left, depth + 1)
        right = self.dfs(node.right, depth + 1)
        if left == right and left == self.maxDepth:
            self.res = node
        return max(left, right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, maxSeen):
            nonlocal count
            if not node:
                return 
            count += 1 if node.val >= maxSeen else 0
            maxSeen = max(node.val, maxSeen)

            dfs(node.left, maxSeen)
            dfs(node.right,maxSeen)
        dfs(root, root.val)
        return count
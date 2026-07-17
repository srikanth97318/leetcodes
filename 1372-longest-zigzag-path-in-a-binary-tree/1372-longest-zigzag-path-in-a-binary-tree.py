# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, direction, length):
            nonlocal ans
            if not node:
                return
            ans = max(ans,length)
            if direction == 0:
                dfs(node.left,0,1)
                dfs(node.right,1,length+1)
            else:
                dfs(node.left,0, length+1)
                dfs(node.right,1,1)

        if root.left:
            dfs(root.left,0,1)
        if root.right:
            dfs(root.right,1,1)

        return ans
        
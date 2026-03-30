# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        ldep=self.maxDepth(node.left)
        rdep=self.maxDepth(node.right)
        return max(ldep,rdep)+1
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        radice=root
        self.ricorsivainvertTree(radice)
        return root
    def ricorsivainvertTree(self, nodo: Optional[TreeNode]):
        if nodo is None:
            return
        nodo.left, nodo.right = nodo.right, nodo.left
        self.ricorsivainvertTree(nodo.left)
        self.ricorsivainvertTree(nodo.right)

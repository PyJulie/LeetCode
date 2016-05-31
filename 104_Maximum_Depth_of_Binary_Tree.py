# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        p = self.maxDepth(root.left)
        q = self.maxDepth(root.right)
        if p >= q:
            return p + 1
        if p < q:
            return q + 1

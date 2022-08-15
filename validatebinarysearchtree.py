# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def valid(self, root, ubound, lbound):
            if root is None:
                return True
            if not (lbound < root < ubound):
                return False
            return valid(root.left, root, lbound) and valid(root.right, ubound, root)
        return valid(root, float("inf"),float("-inf"))

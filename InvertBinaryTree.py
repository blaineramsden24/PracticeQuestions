class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        placeholder = root.left
        root.left = root.right
        root.right = placeholder

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


    def maxdepth(self, root, depth):

        if not root:
            return depth

        self.maxdepth(self, root.left, depth+1)
        self.maxdepth(self, root.right, depth+1)

        max()
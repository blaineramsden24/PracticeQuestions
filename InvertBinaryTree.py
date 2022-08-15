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
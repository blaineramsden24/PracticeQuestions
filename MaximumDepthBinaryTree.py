# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        return dfs(root, 0)


'''
We solve this by running a depth first search and tracking the depth of each of the subtrees and running a max in order to get
the deepest sub tree.

Time Complexity  --> O(N)
Space Complexity --> O(N)
 
 '''


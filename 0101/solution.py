# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(leftRoot, rightRoot):
            if leftRoot == None and rightRoot == None:
                return True
            if leftRoot == None or rightRoot == None:
                return False
            if leftRoot.val != rightRoot.val:
                return False
            return check(leftRoot.left, rightRoot.right) and check(leftRoot.right, rightRoot.left)
        
        if root == None:
            return True
        return check(root.left, root.right)       
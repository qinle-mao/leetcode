# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def step(currNode):
            if currNode == None:
                return 0
            leftSum, rightSum = step(currNode.left), step(currNode.right)
            self.res += abs(leftSum - rightSum)
            return leftSum + rightSum + currNode.val
        self.res = 0
        step(root)
        return self.res
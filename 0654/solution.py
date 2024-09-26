# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def step(left, right): # both inclusive
            def findMax():
                maxIdx, maxNum = -1, float('-inf')
                for i in range(left, right + 1):
                    if nums[i] > maxNum:
                        maxIdx, maxNum = i, nums[i]
                return maxIdx, maxNum
            if left > right:
                return None
            maxIdx, maxNum = findMax()
            root = TreeNode(val=maxNum)
            root.left, root.right = step(left, maxIdx - 1), step(maxIdx + 1, right)
            return root
        return step(0, len(nums) - 1)
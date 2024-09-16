# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def constructTree(self, arr):
        def step(i):
            if i > len(arr) - 1:
                return None
            elif arr[i] == None:
                return None
            newNode = TreeNode(val=arr[i])
            newNode.left = step(i * 2 + 1)
            newNode.right = step(i * 2 + 2)
            return newNode
        return step(0)

    def printTree(self, root):
        from collections import deque
        if root == None:
            return
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            currNode = queue.popleft()
            leftChild, rightChild = currNode.left, currNode.right
            if leftChild != None:
                queue.append(leftChild)
            if rightChild != None:
                queue.append(rightChild)
            print(currNode.val, end=' ')
        print()

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        def step(currNode, currSum, flag):
            if currNode == None:
                return
            if flag == 0:
                step(currNode.left, currSum, 0)
                step(currNode.right, currSum, 0)
            currSum += currNode.val
            if currSum == targetSum:
                self.count += 1
            step(currNode.left, currSum, 1)
            step(currNode.right, currSum, 1)
        self.count = 0
        step(root, 0, 0)    
        return self.count

root = TreeNode().constructTree([10,5,-3,3,2,None,11,3,-2,None,1])
targetSum = 8
print(Solution().pathSum(root, targetSum))
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        # Level order traversal
        from collections import deque
        q = deque()
        q.append(self)
        while len(q) > 0:
            currNode = q.popleft()
            if currNode.left != None:
                q.append(currNode.left)
            if currNode.right != None:
                q.append(currNode.right)
            print(currNode.val, end=' ')

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def step(inorder, postorder):
            if len(inorder) == 0:
                return None
            currRoot = TreeNode(postorder[-1])
            i = 0
            for i in range(len(inorder)):
                if inorder[i] == postorder[-1]:
                    break
            currRoot.left = step(inorder[:i], postorder[:i])
            currRoot.right = step(inorder[i+1:], postorder[i:len(postorder)-1])
            return currRoot
        return step(inorder, postorder)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Solution().buildTree(inorder, postorder).printTree()
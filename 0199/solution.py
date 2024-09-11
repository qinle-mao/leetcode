# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        if root == None:
            return []
        queue = deque()
        queue.append((root, 0))
        res = []
        level = -1
        while len(queue) > 0:
            currNode, currLevel = queue.popleft()
            if currLevel > level:
                res.append(currNode.val)
                level = currLevel
            if currNode.right != None:
                queue.append((currNode.right, currLevel + 1))
            if currNode.left != None:
                queue.append((currNode.left, currLevel + 1))
        return res

node1 = TreeNode(val=1) 
node2 = TreeNode(val=2) 
node3 = TreeNode(val=3) 
node4 = TreeNode(val=4) 
node5 = TreeNode(val=5)
node2.right = node5
node3.right = node4
node1.left, node1.right = node2, node3
print(Solution().rightSideView(root=node1))
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        from collections import deque
        class QElement(object):
            def __init__(self, node=None, level=-1):
                self.node = node
                self.level = level
        if root == None:
            return root
        q = deque()
        q.append(QElement(root, 0))
        globalLevel = 0
        levelNode = []
        while len(q) > 0:
            currElement = q.popleft()
            currNode, currLevel = currElement.node, currElement.level
            if currNode.left != None:
                q.append(QElement(currNode.left, currLevel + 1))
            if currNode.right != None:
                q.append(QElement(currNode.right, currLevel + 1))
            if currLevel > globalLevel:
                i = 0
                while i < len(levelNode) - 1:
                    levelNode[i].next = levelNode[i+1]
                    i += 1
                levelNode[i].next = None
                globalLevel = currLevel
                levelNode = []
            levelNode.append(currNode)
        i = 0
        while i < len(levelNode) - 1:
            levelNode[i].next = levelNode[i+1]
            i += 1
        levelNode[i].next = None
        return root

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)
node_1.left, node_1.right = node_2, node_3
node_2.left, node_2.right = node_4, node_5
node_3.left, node_3.right = node_6, node_7
node_1 = Solution().connect(node_1)
print(node_6.next)
class TreeNode(object):
    def __init__(self, value=None, firstChild=None, nextSibling=None, isLeaf=False):
        self.value = value
        self.firstChild = firstChild
        self.nextSibling = nextSibling
        self.isLeaf = isLeaf

    def printTree(self):
        from collections import deque
        class StackElement(object):
            def __init__(self, node, level):
                self.node = node
                self.level = level
        
        if self == None:
            return
        q = deque()
        currLevel = 0
        q.append(StackElement(self, 0))
        while len(q) > 0:
            currElement = q.popleft()
            if currElement.level > currLevel:
                currLevel = currElement.level
                print()
            print(currElement.node.value, end=' ')
            currChild = currElement.node.firstChild
            currLevel = currElement.level
            while currChild != None:
                q.append(StackElement(currChild, currLevel + 1))
                currChild = currChild.nextSibling
        print()

    def findChildren(self, char):
        if self == None:
            return None
        currChild = self.firstChild
        while currChild != None:
            if currChild.value == char:
                return currChild
            currChild = currChild.nextSibling
        return None

    def insertChild(self, char):
        if self == None:
            return None
        newNode = TreeNode(value=char)
        if self.firstChild == None:
            self.firstChild = newNode
        else:
            currNode = self.firstChild
            while currNode.nextSibling != None:
                currNode = currNode.nextSibling
            currNode.nextSibling = newNode
        return newNode   

class TrieTree(object):
    def __init__(self):
        self.root = TreeNode()

    def printTree(self):
        TreeNode.printTree(self.root)

    def insert(self, word):
        currParent = self.root
        for char in word:
            nextParent = TreeNode.findChildren(currParent, char)
            if nextParent == None:
                currParent = TreeNode.insertChild(currParent, char)
            else:
                currParent = nextParent
        currParent.isLeaf = True
    
    def find(self, word):
        currParent = self.root
        for char in word:
            nextParent = TreeNode.findChildren(currParent, char)
            if nextParent == None:
                return False
            currParent = nextParent
        return currParent.isLeaf
    
    def delete(self, word):
        # TODO
        pass



t = TrieTree()
t.insert('haha')
t.insert('hello')
t.insert('no')
t.printTree()
print(t.find('hell'))
print(t.find('hello'))
t.insert('hell')
print(t.find('hell'))
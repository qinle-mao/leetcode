class TreeNode(object):
    def __init__(self, value=None, firstChild=None, nextSibling=None, isLeaf=False):
        self.value = value
        self.firstChild = firstChild
        self.nextSibling = nextSibling
        self.isLeaf = isLeaf
    
    def findChild(self, c):
        pos = self.firstChild
        while pos != None:
            if pos.value == c:
                return pos
            pos = pos.nextSibling
        return None
    
    def insertChild(self, c):
        newNode = TreeNode(c)
        pos = self.firstChild
        if pos == None:
            self.firstChild = newNode
            return newNode
        while pos.nextSibling != None:
            pos = pos.nextSibling
        pos.nextSibling = newNode
        return newNode

    def children(self):
        res = []
        pos = self.firstChild
        while pos != None:
            res.append(pos)
            pos = pos.nextSibling
        return res

class WordDictionary(object):
    def __init__(self):
        self.root = TreeNode()
    
    def addWord(self, word):
        def step(root, idx):
            if idx == len(word):
                root.isLeaf = True
                return
            next = root.findChild(word[idx])
            if next == None:
                next = root.insertChild(word[idx])
            step(next, idx + 1)
        step(self.root, 0)

    def search(self, word):
        def step(root, idx):
            if idx == len(word):
                if root.isLeaf:
                    return True
                else:
                    return False
            if word[idx] != '.':
                next = root.findChild(word[idx])
                if next == None:
                    return False
                return step(next, idx + 1)
            else:
                res = False
                for child in root.children():
                    res |= step(child, idx + 1)
                return res
        return step(self.root, 0)
    
tree = WordDictionary()
tree.addWord("at")
tree.addWord("and")
tree.addWord("an")
tree.addWord("add")
print(tree.search("a")) # f
print(tree.search(".at")) # f
tree.addWord("bat")
print(tree.search(".at")) # t
print(tree.search("an.")) # t
print(tree.search("a.d.")) # f
print(tree.search("b.")) # f
print(tree.search("a.d")) # t
print(tree.search(".")) # f
print(tree.search("bat")) # t
tree.addWord("a")
print(tree.search("a")) # t
print(tree.search(".")) # t

# Trie Tree
class WordDictionary(object):
    class TreeNode():
        def __init__(self, value=None, isLeaf=False, children=[]):
            self.value = value
            self.isLeaf = isLeaf
            self.children = children
        
        def findChild(self, char):
            for child in self.children:
                if child.value == char:
                    return child
            return None

    def __init__(self):
        self.root = self.TreeNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        currParent = self.root
        for char in word:
            nextParent = currParent.findChild(char)
            if nextParent == None:
                newNode = self.TreeNode(value=char)
                currParent.children.append(newNode)
                currParent = newNode
            else:
                currParent = nextParent
        currParent.isLeaf = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(char, node):
            pass
        currParent = self.root
        for char in word:
            nextParent = currParent.findChild(char)
            if nextParent == None:
                return False
            currParent = nextParent
        return currParent.isLeaf
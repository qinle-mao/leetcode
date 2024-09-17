class TreeNode(object):
    def __init__(self, val=None, firstChild=None, nextSibling=None, isLeaf=False):
        self.val = val
        self.firstChild = firstChild
        self.nextSibling = nextSibling
        self.isLeaf = isLeaf
    
    def findChild(self, val):
        pos = self.firstChild
        while pos != None:
            if pos.val == val:
                return pos
            pos = pos.nextSibling
        return None

    def addChild(self, child):
        pos = self.firstChild
        if pos == None:
            self.firstChild = child
            return
        while pos.nextSibling != None:
            pos = pos.nextSibling
        pos.nextSibling = child
        
class Trie(object):
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word):
        pos = self.root
        for char in word:
            child = pos.findChild(char)
            if child == None:
                child = TreeNode(val=char)
                pos.addChild(child)
            pos = child
        pos.isLeaf = True
    
    def search(self, word):
        '''
        0 - not exists, 1 - exists, 2 - exists prefix
        '''
        pos = self.root
        for char in word:
            child = pos.findChild(char)
            if child == None:
                return 0
            pos = child
        if pos.isLeaf == True:
            return 1
        return 2

class Solution(object):
    # double pointers
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        res = ''
        for word in dictionary:
            i = j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            if i == len(word):
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
        return res

    # construct trie - exceeding time limit
    def findLongestWord2(self, s, dictionary):
        def updateRes(currS):
            if len(currS) > len(self.res) or (len(currS) == len(self.res) and currS < self.res):
                self.res = currS
        def step(i, n, currS):
            if i >= n:
                if self.trie.search(currS) == 1:
                    updateRes(currS)
                return
            # adding current char
            newS = currS + s[i]
            tmp = self.trie.search(newS)
            if tmp > 0:
                if tmp == 1:
                    updateRes(newS)
                step(i + 1, n, newS)
            # not adding current char
            step(i + 1, n, currS)

        self.res = ''
        self.trie = Trie()
        for word in dictionary:
            self.trie.addWord(word)
        step(0, len(s), '')
        return self.res

s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
print(Solution().findLongestWord(s, dictionary))
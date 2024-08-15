class BST(object):
    class BSTNode(object):
        def __init__(self, val=None, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, root=None):
        self.root = root
    
    def _find_min_pos(self):
        if self.root == None:
            return None
        currPos = self.root
        while currPos.left != None:
            currPos = currPos.left
        return currPos
    
    def _find_max_pos(self):
        if self.root == None:
            return None
        currPos = self.root
        while currPos.right != None:
            currPos = currPos.right
        return currPos

    def insert(self, val):
        def insertStep(currPos):
            if currPos == None:
                currPos = self.BSTNode(val)
            elif val > currPos.val:
                currPos.right = insertStep(currPos.right)
            elif val < currPos.val:
                currPos.left = insertStep(currPos.left)
            return currPos
        self.root = insertStep(self.root)

    def findMin(self):
        return self._find_min_pos().val
    
    def findMax(self):
        return self._find_max_pos().val

    def delete(self, val):
        def deleteStep(currPos, val):
            if currPos == None:
                pass
            elif val > currPos.val:
                currPos.right = deleteStep(currPos.right, val)
            elif val < currPos.val:
                currPos.left = deleteStep(currPos.left, val)
            else:
                if currPos.left == None and currPos.right == None:
                    currPos = None
                elif currPos.left == None:
                    currPos = currPos.right
                elif currPos.right == None:
                    currPos = currPos.left
                else:
                    maxValLeft = BST(currPos.left).findMax()
                    currPos.val = maxValLeft
                    currPos.left = deleteStep(currPos.left, maxValLeft)
            return currPos
        self.root = deleteStep(self.root, val)



t = BST()
t.insert(1)
t.insert(3)
t.insert(6)
t.delete(1)
print(t.findMin())
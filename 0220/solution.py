class Solution(object):
    # + sorted list (in sortedcontainers)
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        from sortedcontainers import SortedList
        n = len(nums)
        window = SortedList()
        for i in range(n):
            pass
        return False

    # + binary search tree - exceeding time limit
    def containsNearbyAlmostDuplicate2(self, nums, indexDiff, valueDiff):
        class BST(object):
            class BSTNode(object):
                def __init__(self, val=None, left=None, right=None):
                    self.val = val
                    self.left = left
                    self.right = right

            def __init__(self, root=None):
                self.root = root

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
                            maxValLeft = BST(currPos.left)._find_max_pos().val
                            currPos.val = maxValLeft
                            currPos.left = deleteStep(currPos.left, maxValLeft)
                    return currPos
                self.root = deleteStep(self.root, val)

            def findNotLessMin(self, val):
                def fnlmStep(currPos):
                    if currPos == None:
                        return
                    if currPos.val > val:
                        self.currMin = min(currPos.val, self.currMin)
                        fnlmStep(currPos.left)
                    elif currPos.val < val:
                        fnlmStep(currPos.right)
                    else:
                        self.currMin = val
                        return
                self.currMin = float('Inf')
                fnlmStep(self.root)
                return self.currMin

        n = len(nums)
        tree = BST()
        for i in range(n):
            noLessMin = tree.findNotLessMin(nums[i] - valueDiff)
            if noLessMin != None and noLessMin <= nums[i] + valueDiff:
                return True
            tree.insert(nums[i])
            if i >= indexDiff:
                tree.delete(nums[i-indexDiff])
        return False
    
    # simple sliding window algorithm - exceeding time limit
    def containsNearbyAlmostDuplicate3(self, nums, indexDiff, valueDiff):
        WINDOW_WIDTH = indexDiff
        n = len(nums)
        for i in range(n):
            for j in range(1, min(WINDOW_WIDTH, n - i - 1) + 1):
                if abs(nums[i] - nums[i+j]) <= valueDiff:
                    return True
        return False

# nums = [1,2,2,3,4,5]
# indexDiff, valueDiff = 3, 0
# nums = [1,5,9,1,5,9]
# indexDiff, valueDiff = 2, 3
# nums = [4,1,-1,6,5]
# indexDiff, valueDiff = 3, 1
# nums = [7,1,3]
# indexDiff, valueDiff = 2, 3
nums = [3,6,0,4]
indexDiff, valueDiff = 2, 2
print(Solution().containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))
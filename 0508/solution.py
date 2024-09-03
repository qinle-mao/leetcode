# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def findMaxCount(arr):
            countDict = {}
            for e in arr:
                if e in countDict.keys():
                    countDict[e] += 1
                else:
                    countDict[e] = 1
            maxCount = 0
            res = []
            for key, val in countDict.items():
                if val > maxCount:
                    maxCount = countDict[key]
                    res[:] = [key]
                elif countDict[key] == maxCount:
                    res.append(key)
            return res
        
        def step(root, sumArr):
            if root == None:
                return 0
            currSum = root.val
            currSum += step(root.left, sumArr)
            currSum += step(root.right, sumArr)
            sumArr.append(currSum)
            return currSum

        sumArr = []
        step(root, sumArr)
        return findMaxCount(sumArr)

node1 = TreeNode(5)
node2 = TreeNode(2)
node3 = TreeNode(-5)
node1.left = node2
node1.right = node3
print(Solution().findFrequentTreeSum(root=node1))
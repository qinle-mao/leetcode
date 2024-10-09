class Solution(object):
    # We first iterate through all the cards, if the two numbers on the card are the same, then add to the hash set same, 
    # all the numbers except this set, can be selected as x, we just need to iterate through all the numbers again to find the minimum value.
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        n = len(fronts)
        same = set()
        for i in range(n):
            if fronts[i] == backs[i]:
                same.add(fronts[i])
        res = 3000
        for e in fronts:
            if e < res and e not in same:
                res = e
        for e in backs:
            if e < res and e not in same:
                res = e
        return res if res < 3000 else 0

    # exceeding time limit
    def flipgame2(self, fronts, backs):
        def incrementKey(k, d):
            if k in d.keys():
                d[k] += 1
            else:
                d[k] = 1

        def decrementKey(k, d):
            if k in d.keys():
                if d[k] > 1:
                    d[k] -= 1
                else:
                    d.pop(k)

        def createDict(arr):
            res = {}
            for e in arr:
                incrementKey(e, res)
            return res
        
        def copyAndExchange(k1, d1, k2, d2):
            newD1, newD2 = dict(d1), dict(d2)
            decrementKey(k1, newD1)
            incrementKey(k2, newD1)
            decrementKey(k2, newD2)
            incrementKey(k1, newD2)
            return newD1, newD2
        
        def step(i, n, frontDict, backDict):
            if i == n:
                goodArr = sorted([e for e in frontDict.keys() if e not in backDict.keys()])
                if len(goodArr) > 0:
                    self.res = min(self.res, goodArr[0])
                return
            step(i + 1, n, frontDict, backDict)
            newFrontDict, newBackDict = copyAndExchange(fronts[i], frontDict, backs[i], backDict)
            step(i + 1, n, newFrontDict, newBackDict)

        self.res = float('inf')
        frontDict, backDict = createDict(fronts), createDict(backs)
        step(0, len(fronts), frontDict, backDict)
        return self.res if self.res != float('inf') else 0
    
# fronts, backs = [1,2,4,4,7], [1,3,4,1,3]
fronts, backs = [1,5,4,7,4,3,7,4,6,1,4,8,1,3,1,2,4,5,8,7], [1,5,4,1,4,3,8,3,6,3,2,6,2,3,3,2,2,5,5,8]
print(Solution().flipgame(fronts, backs))
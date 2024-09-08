class Solution(object):
    # find the max height for each boundary
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # import heapq
        boundaries = []
        for building in buildings:
            boundaries.append(building[0])
            boundaries.append(building[1])
            boundaries.sort()
        res, heap = [], []
        n, pos = len(buildings), 0
        for boundary in boundaries:
            while pos < n and buildings[pos][0] <= boundary:
                heap.append((buildings[pos][2], buildings[pos][1]))
                # heapq.heappush(heap, (buildings[pos][2], buildings[pos][1]))
                heap.sort(reverse=True)
                print(heap)
                pos += 1
            while len(heap) > 0 and heap[0][1] <= boundary:
                # heapq.heappop(heap)
                heap.pop(0)
                print(heap)
            maxHeight = 0
            if len(heap) != 0:
                maxHeight = heap[0][0]
            if len(res) == 0 or maxHeight != res[-1][1]:
                res.append([boundary, maxHeight])
        return res
    
    # too violent - memory out of range
    def getSkyline2(self, buildings):
        def getHeight(pos, pic):
            height = 0
            for j in range(1, MAX_H):
                if pic[pos][j] == 0:
                    break
                height += 1
            return height
        
        MAX_X, MAX_H = buildings[-1][1] + 2, max([b[2] for b in buildings]) + 2
        pic = [[0 for _ in range(MAX_H)] for _ in range(MAX_X)]
        for building in buildings:
            left, right, height = building[0], building[1], building[2]
            for i in range(left, right + 1):
                for j in range(0, height + 1):
                    pic[i][j] = 1
        res, prevHeight = [], 0
        for pos in range(MAX_X):
            currHeight = getHeight(pos, pic)
            if currHeight > prevHeight:
                res.append([pos, currHeight])
            elif currHeight < prevHeight:
                res.append([pos - 1, currHeight])
            prevHeight = currHeight
        return res
    
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# buildings = [[0,2,3],[2,5,3]]
# buildings = [[0,2147483647,2147483647]]
print(Solution().getSkyline(buildings))
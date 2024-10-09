class Solution(object):
    def cutOffTree(self, forest): # Breadth-First-Search
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        from collections import deque
        def BFS(x1, y1, x2, y2):
            m, n = len(forest), len(forest[0])
            queue = deque([(0, x1, y1)])
            visited = {(x1, y1)}
            while len(queue) > 0:
                d, x, y = queue.popleft()
                if x == x2 and y == y2:
                    return d
                for newX, newY in ((x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)):
                    if 0 <= newX < m and 0 <= newY < n and forest[newX][newY] > 0 and (newX, newY) not in visited:
                        visited.add((newX, newY))
                        queue.append((d + 1, newX, newY))
            return -1
        res = 0
        cells = sorted((h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1)
        prevI = prevj = 0
        for _, i, j in cells:
            d = BFS(prevI, prevj, i, j)
            if d < 0:
                return -1
            res += d
            prevI, prevj = i, j
        return res

    def cutOffTree2(self, forest): # A* Algorithm TODO
        def aStarSearch(start, goal, h):
            from queue import PriorityQueue
            
            def heuristic(pos1, pos2):
                return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
            
            def neighbors(pos):
                m, n = len(forest), len(forest[0])
                x, y = pos[0], pos[1]
                res = []
                for newX, newY in ((x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)):
                    if 0 <= newX < m and 0 <= newY < n and (forest[newX][newY] == 1 or forest[newX][newY] == h):
                        res.append((newX, newY))
                return res
            
            frontier = PriorityQueue()
            frontier.put((0, start))
            path, cost = {}, {}
            path[start], cost[start] = [], 0
            while not frontier.empty():
                _, pos = frontier.get()
                if pos == goal:
                    return len(path[pos])
                for next in neighbors(pos):
                    newCost = cost[pos] + 1
                    if next not in cost or newCost < cost[next]:
                        cost[next] = newCost
                        priority = newCost + heuristic(next, goal)
                        frontier.put((priority, next))
                        path[next] = [_ for _ in path[pos]] + [next]
            return -1
        
        res = 0
        cells = sorted((h, (i, j)) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1)
        prev = (0, 0)
        for h, pos in cells:
            d = aStarSearch(prev, pos, h)
            if d < 0:
                return -1
            res += d
            forest[pos[0]][pos[1]] = 1
            prev = pos
        return res

# forest = [[1,2,3],[0,0,4],[7,6,5]]
# forest = [[1,2,3],[0,0,0],[7,6,5]]
# forest = [[1,2,4],[0,3,0],[0,0,0]]
forest = [[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]
print(Solution().cutOffTree2(forest))
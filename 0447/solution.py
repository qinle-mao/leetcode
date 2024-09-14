class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def squareDistance(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
        
        def add2Map(distance, dict):
            if distance in dict.keys():
                dict[distance] += 1
            else:
                dict[distance] = 1

        def getRes(count):
            return count * (count - 1)
        
        res = 0
        n = len(points)
        map = [{} for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                distance = squareDistance(points[i], points[j])
                add2Map(distance, map[i]) 
                add2Map(distance, map[j])
        for point in map:
            for _ , count in point.items():
                res += getRes(count)
        return res

points = [[0,0],[1,0],[2,0]]
print(Solution().numberOfBoomerangs(points))
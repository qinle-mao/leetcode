class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        res = 0
        map = [[0 for _ in range(n)] for _ in range(n)]
        for pos in artifacts:
            r1, c1, r2, c2 = pos[0], pos[1], pos[2], pos[3]
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    map[i][j] = 1
        for pos in dig:
            map[pos[0]][pos[1]] *= -1
        for pos in artifacts:
            r1, c1, r2, c2 = pos[0], pos[1], pos[2], pos[3]
            done = True
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if map[i][j] != -1:
                        done = False
            if done == True:
                res += 1
        return res
    
n = 2
artifacts = [[0,0,0,0],[0,1,1,1]]
dig = [[0,0],[0,1]]
print(Solution().digArtifacts(n, artifacts, dig))
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        count = len(matrix[0]) * len(matrix)
        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        rightB, downB, leftB, upB = len(matrix[0])-1, len(matrix)-1, 0, 0
        direction = RIGHT
        i, j = 0, 0
        while len(res) < count:
            if direction == RIGHT:
                if j <= rightB:
                    res.append(matrix[i][j])
                    j += 1
                else:
                    direction = DOWN
                    upB += 1
                    j -= 1
                    i += 1
            elif direction == DOWN:
                if i <= downB:
                    res.append(matrix[i][j])
                    i += 1
                else:
                    direction = LEFT
                    rightB -= 1
                    i -= 1
                    j -= 1
            elif direction == LEFT:
                if j >= leftB:
                    res.append(matrix[i][j])
                    j -= 1
                else:
                    direction = UP
                    downB -= 1
                    j += 1
                    i -= 1
            elif direction == UP:
                if i >= upB:
                    res.append(matrix[i][j])
                    i -= 1
                else:
                    direction = RIGHT
                    leftB += 1
                    i += 1
                    j += 1
        return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(matrix))
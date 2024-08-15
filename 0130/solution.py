# For each 'O' on the boundary, we use it as a starting point to mark all the letters 'O' that are directly or indirectly connected to it;
# then we iterate through this matrix, for each letter:
# if the letter is marked 'A', then the letter is an 'O' not surrounded by 'X', so we revert it to 'O';
# if the letter has not been marked, then it is an 'O' surrounded by 'X', so we modify it to 'X'.
class Solution(object):
    # depth-first-search
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != 'O':
                return
            board[x][y] = 'A'
            dfs(x, y + 1)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x - 1, y)
        
        m, n = len(board), len(board[0])
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for i in range(1, n - 1):
            dfs(0, i)
            dfs(m - 1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    # breadth-first-search
    def solve2(self, board):
        from collections import deque
        m, n = len(board), len(board[0])
        q = deque()
        for i in range(m):
            if board[i][0] == 'O':
                q.append((i, 0))
                board[i][0] = 'A'
            if board[i][n - 1] == 'O':
                q.append((i, n - 1))
                board[i][n - 1] = 'A'
        for i in range(1, n - 1):
            if board[0][i] == 'O':
                q.append((0, i))
                board[0][i] = 'A'
            if board[m - 1][i] == 'O':
                q.append((m - 1, i))
                board[m - 1][i] = 'A'
        while len(q) > 0:
            x, y = q.popleft()
            for currX, currY in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= currX < n and 0 <= currY < m and board[currX][currY] == 'O':
                    q.append((currX, currY))
                    board[currX][currY] = 'A'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# board = [["X"]]
board = [["O","O","O"],["O","O","O"],["O","O","O"]]
Solution().solve(board)
print(board)
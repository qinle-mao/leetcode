# Backtracking
# add the queen row by row
class Solution:
    def solveNQueens(self, n):
        def addBoard(l, res):
            curr_list = []
            for i in range(n):
                curr_line = '.' * n
                curr_line = curr_line[:res[i]] + 'Q' + curr_line[res[i]+1:]
                curr_list.append(curr_line)
            l.append(curr_list)

        def check(res, curr_idx):
            new_row = curr_idx
            new_col = res[curr_idx]
            for i in range(curr_idx):
                if new_row == i or new_col == res[i] or abs(new_row-i) == abs(new_col-res[i]):
                    return False
            return True
        
        def step(res, curr_idx):
            if curr_idx == n:
                addBoard(l, res)
                return
            for i in range(n):
                res[curr_idx] = i
                if check(res, curr_idx):
                    step(res, curr_idx+1)
        
        res = [0] * n
        curr_idx = 0
        l = []
        step(res, curr_idx)
        return l

n = 4
print(Solution().solveNQueens(n))
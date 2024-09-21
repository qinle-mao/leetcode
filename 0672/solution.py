class Solution(object):
    '''
    编号为 6k+1, 受按钮 1,3,4 影响;
    编号为 6k+2,6k+6, 受按钮 1,2 影响;
    编号为 6k+3,6k+5, 受按钮 1,3 影响;
    编号为 6k+4, 受按钮 1,2,4 影响.
    '''
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        res = set()
        for i in range(2 ** 4):
            pressArr = [(i >> j) & 1 for j in range(4)]
            if sum(pressArr) % 2 == presses % 2 and sum(pressArr) <= presses:
                status = pressArr[0] ^ pressArr[2] ^ pressArr[3]
                if n >= 2:
                    status |= (pressArr[0] ^ pressArr[1]) << 1
                if n >= 3:
                    status |= (pressArr[0] ^ pressArr[2]) << 2
                if n >= 4:
                    status |= (pressArr[0] ^ pressArr[1] ^ pressArr[3]) << 3
                res.add(status)
        return len(res)

    # too violent - eceeding time limit
    def flipLights2(self, n, presses):
        def step(status, pressCount):
            if pressCount == presses:
                if status not in self.res:
                    self.res.append(status)
                return
            step([x * -1 for x in status], pressCount + 1)
            step([status[i] * -1 if (i + 1) % 2 == 0 else status[i] for i in range(n)], pressCount + 1)
            step([status[i] * -1 if (i + 1) % 2 == 1 else status[i] for i in range(n)], pressCount + 1)
            step([status[i] * -1 if (i + 1) % 3 == 1 else status[i] for i in range(n)], pressCount + 1)
        self.res = []
        step([1 for _ in range(n)], 0)
        return len(self.res)

# print(Solution().flipLights(n=4, presses=100))
print(Solution().flipLights(n=5, presses=8))
class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
    
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

n = 4
presses = 100
print(Solution().flipLights(n, presses))
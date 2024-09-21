class Solution(object):
    # monotonic stack
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n):
            temperature = temperatures[i]
            while len(stack) > 0 and temperature > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res

    # too violent - exceeding time limit
    def dailyTemperatures2(self, temperatures):
        res = []
        n = len(temperatures)
        for i in range(n):
            flag = 0
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    flag = 1
                    break
            if flag == 0:
                res.append(0)
        return res

print(Solution().dailyTemperatures(temperatures=[73,74,75,71,69,72,76,73]))
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def getFactors(x):
            factors = []
            for factor in range(2, x // 2):
                while x % factor == 0:
                    factors.append(factor)
                    x //= factor
            return factors
        res = [0, 0, 2]
        for x in range(3, n + 1):
            if x % 2 == 0:
                res.append(res[x//2] + 2)
            else:
                factors = getFactors(x)
                if len(factors) == 0:
                    res.append(x)
                else:
                    res.append(sum(factors))
        return res[n]

print(Solution().minSteps(n=525))
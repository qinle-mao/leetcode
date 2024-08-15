# There is an interval [i, j], where all the cars between [0, i) and (j, n) are removed, and all the illegal cars in [i, j] are removed
# min = (i) + (n - j -1) + 2 * count(i, j)
# count(i, j) can be represented as preSum(j) - preSum(i-1)
# min = (i) + (n - j - 1) + 2 * (preSum(j) - preSum(i-1))
# = (i - 2 * preSum(i-1)) + (2 * preSum(j) - j) + (n - 1)
class Solution(object):
    def minimumTime(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = float('inf')
        preSumJ = preBestI = 0
        for j, c in enumerate(s):
            preBestI = min(preBestI, j - 2 * preSumJ)
            preSumJ += int(c)
            res = min(res, preBestI + 2 * preSumJ - j)
        return min(res + n - 1, n)

# s = "1100101"
s = "0111001110"
print(Solution().minimumTime(s))
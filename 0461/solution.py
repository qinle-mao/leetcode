class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        def get1s(x):
            count = 0
            while x > 0:
                if x % 2 == 1:
                    count += 1
                x >>= 1
            return count
        return get1s(x ^ y)

x, y = 1, 4
print(Solution().hammingDistance(x, y))
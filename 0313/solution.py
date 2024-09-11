class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        m = len(primes)
        uglyNums = [0] * (n + 1)
        pointers, nums = [0] * m, [1] * m
        for i in range(1, n + 1):
            minNum = min(nums)
            uglyNums[i] = minNum
            for j in range(m):
                if nums[j] == minNum:
                    pointers[j] += 1
                    nums[j] = uglyNums[pointers[j]] * primes[j]
        return uglyNums[n]
        

# n, primes = 12, [2, 7, 13, 19]
# n, primes = 10, [2, 5, 7, 11, 13, 17, 23 ,29, 43, 53]
n, primes = 15, [3, 5, 7, 11, 19, 23, 29, 41, 43, 47]
print(Solution().nthSuperUglyNumber(n, primes))
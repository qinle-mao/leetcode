class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglyNums = [1, primes[0]]
        pos0, pos1, pos2 = 1, 1, 0
        while len(uglyNums) < n:
            newNum = uglyNums[pos0] * primes[pos2]
            if pos1 < len(primes) and primes[pos1] < newNum:
                uglyNums.append(primes[pos1])
                pos1 += 1
            else:
                uglyNums.append(newNum)
                if pos2 < len(primes) and primes[pos2+1] * uglyNums[pos0] < primes[pos2] * uglyNums[pos0+1]:
                    pos2 += 1
                else:
                    pos0 += 1
        print(uglyNums)
        return uglyNums[n-1]

# n, primes = 12, [2, 7, 13, 19]
# n, primes = 10, [2, 5, 7, 11, 13, 17, 23 ,29, 43, 53]
n, primes = 15, [3, 5, 7, 11, 19, 23, 29, 41, 43, 47]
print(Solution().nthSuperUglyNumber(n, primes))
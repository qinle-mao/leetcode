class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        base = 0
        while base < len(str(n)):
            for x in range(n+1):
                currS = str(x)
                if base < len(currS) and currS[len(currS)-1-base] == '1':
                    count += 1
            base += 1 
        return count

n = 13
print(Solution().countDigitOne(n))
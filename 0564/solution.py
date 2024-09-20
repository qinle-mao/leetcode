class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1] # 99..9 10..01
        prefix = int(n[:(m+1)//2])
        for x in range(prefix - 1, prefix + 2): # prefix-1 / prefix / prerfix+1
            y = x if m % 2 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)
        res = -1
        num = int(n)
        for candidate in candidates:
            if candidate != num:
                if res == -1 or abs(candidate - num) < abs (res - num) or \
                abs(candidate - num) == abs(res - num) and candidate < res:
                    res = candidate
        return str(res)

print(Solution().nearestPalindromic(n='123'))
print(Solution().nearestPalindromic(n='827134'))
print(Solution().nearestPalindromic(n='810001'))
print(Solution().nearestPalindromic(n='1000'))
print(Solution().nearestPalindromic(n='1'))

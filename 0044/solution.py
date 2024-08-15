class Solution(object):
    # dynamic programming
    # let f[i][j] be if s[:i] and p[:j] matches
    # if p[j-1] == '*': 
    # f[i][j] = f[i][j-1] or f[i-1][j-1] or f[i-2][j-1] or ... = f[i][j-1] + f[i-1][j]
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        f = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][0] = True
        for j in range(1, n + 1):
            if p[j-1] == '*':
                f[0][j] = f[0][j-1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    f[i][j] = f[i-1][j] or f[i][j-1]
                elif p[j-1] == '?' or p[j-1] == s[i-1]:
                    f[i][j] = f[i-1][j-1]
        return f[m][n]
    
    # backtracking: exceeding time limit
    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # TODO: remove duplicate stars
        def removeDuplicateStars(s):
            return s
        def checkEnd(indexP):
            for i in range(indexP, len(p)):
                if p[i] != '*':
                    return False
            return True
        def step(indexS, indexP):
            if indexS == len(s):
                if checkEnd(indexP):
                    return True
                else:
                    return False
            if indexP == len(p):
                return False
            if p[indexP] == '*':
                res = False
                for i in range(indexS, len(s)+1):
                    res |= step(i, indexP+1)
                return res
            elif p[indexP] == '?' or p[indexP] == s[indexS]:
                return step(indexS+1, indexP+1)
            elif p[indexP] != s[indexS]:
                return False
        s = removeDuplicateStars(s)
        return step(0, 0)

s = 'baaabab'
p_1 = '***ba**ab'
p_2 = 'baaa?ab'
p_3 = 'ba*a?'
p_4 = 'a*ab'
p_5 = '*'
print(Solution().isMatch(s, p_1))
print(Solution().isMatch(s, p_2))
print(Solution().isMatch(s, p_3))
print(Solution().isMatch(s, p_4))
print(Solution().isMatch(s, p_5))
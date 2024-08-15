class Solution(object):
    # dynamic programming
    # f(i,j)=(f(i − 1,j) and s1[i-1] == s3[p]) or (f(1, j-1) and s2[j-1] == s3[p]), where p = i + j - 1
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        f = []
        for i in range(len(s1) + 1):
            f.append([False] * (len(s2) + 1))
        f[0][0] = True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                p = i + j - 1
                if i > 0:
                    f[i][j] = (f[i][j] or (f[i-1][j] and (s1[i-1] == s3[p])))
                if j > 0:
                    f[i][j] = (f[i][j] or (f[i][j-1] and (s2[j-1] == s3[p])))
        return f[len(s1)][len(s2)]

    # outside time limit - simple backtracking
    def isInterleave2(self, s1, s2, s3):
        def check(range, s, idx3):
            if s[range[0]:range[1]] == s3[idx3:idx3+(range[1]-range[0])]:
                return True
            return False
        
        def step(range1, range2, idx3, turn):
            if idx3 == len(s3):
                if range1[1] == len(s1) and range2[1] == len(s2):
                    return True
                else:
                    return False
            res = False
            if turn == T1:
                range1[0] = range1[1]
                for i in range(range1[0] + 1, len(s1) + 1):
                    if check([range1[0], i], s1, idx3):
                        res |= step([range1[0], i], range2, idx3 + i -range1[0], turn*(-1))
                    else:
                        break
            else:
                range2[0] = range2[1]
                for i in range(range2[0] + 1, len(s2) + 1):
                    if check([range2[0], i], s2, idx3):
                        res |= step(range1, [range2[0], i], idx3 + i -range2[0], turn*(-1))
                    else:
                        break
            return res

        T1, T2 = 1, -1
        return step([0, 0], [0, 0], 0, T1) | step([0, 0], [0, 0], 0, T2)

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"

# s1 = "a"
# s2 = "d"
# s3 = "a"

# s1 = "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb"
# s2 = "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
# s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"

s1 = "a"
s2 = ""
s3 = "c"

print(Solution().isInterleave(s1, s2, s3))
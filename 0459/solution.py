class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for step in range(1, len(s) // 2 + 1):
            flag = 0
            p = s[:step]
            for j in range(step, len(s), step):
                if p != s[j:j+step]:
                    flag = 1
            if flag == 0:
                return True
        return False
    
# s = "abcabcabcabc"
s = "abab"
# s = "ababababc"
print(Solution().repeatedSubstringPattern(s))
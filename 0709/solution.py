class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        newStr = ''
        for i in range(len(s)):
            c = s[i]
            if ord('A') <= ord(c) <= ord('Z'):
                c = chr(ord('a') + ord(c) - ord('A'))
            newStr += c
        return newStr

print(Solution().toLowerCase('LOVELY'))
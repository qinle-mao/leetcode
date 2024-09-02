class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def swap(i, j):
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp

        n = len(s)
        for i in range(n // 2):
            swap(i, n - 1 - i)

s = ["h","e","l","l","o"]
Solution().reverseString(s)
print(s)
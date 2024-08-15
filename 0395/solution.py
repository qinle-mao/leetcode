# divide and conquer
# For the string s, if there is a character ch, which occurs more than 0 and less than k, 
# any substring containing ch is unlikely to meet the requirement. 
# That is, if we split a string into segments by ch, 
# the longest substring that satisfies the requirement must appear in exactly one of the segments being sharded

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def step(left, right):
            lookupDict = dict([(chr(ord('a') + i), 0) for i in range(26)])
            for i in range(left, right+1):
                lookupDict[s[i]] += 1
            split = None
            for key in lookupDict.keys():
                if 0 < lookupDict[key] < k:
                    split = key
                    break
            if split == None:
                return right - left + 1
            pos = left
            res = 0
            while pos <= right:
                while pos <= right and s[pos] == split:
                    pos += 1
                if pos > right:
                    break
                start = pos
                while pos <= right and s[pos] != split:
                    pos += 1
                res = max(res, step(start, pos - 1))
            return res
        return step(0, len(s) - 1)

s = 'ababbc'
k = 2
print(Solution().longestSubstring(s, k))
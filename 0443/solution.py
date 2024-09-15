class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int - new length of chars
        """
        n = len(chars)
        pos, prev = 0, 0
        s = []
        while pos < n:
            if chars[pos] != chars[prev]:
                s.extend(chars[prev])
                if pos - prev > 1:
                    s.extend(str(pos - prev))
                prev = pos
            else:
                pos += 1
        s.extend(chars[prev])
        if pos - prev > 1:
            s.extend(str(pos - prev))
        chars[:] = [_ for _ in s]
        return len(chars)
    
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c"]
print(Solution().compress(chars), chars)
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

BAD = 1702766719
def isBadVersion(version):
    if version == BAD:
        return True
    return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def step(left, right):
            if right - left <= 1:
                if isBadVersion(left):
                    return left
                return right
            mid = (left + right) // 2
            if isBadVersion(mid):
                return step(left, mid)
            else:
                return step(mid, right)
        return step(1, n)

print(Solution().firstBadVersion(2126753390))
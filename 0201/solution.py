class Solution(object):
    # 1: find common prefix
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shift = 0   
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift
    
    # 2: Brian Kernighan Algorithm
    # Every time we perform a bitwise sum operation between n and n-1, the rightmost 1 in n is erased and becomes 0
    def rangeBitwiseAnd2(self, left, right):
        while left < right:
            # eleminate the rightmost 1 in right
            right = right & (right - 1)
        return right

left, right = 5, 7
print(Solution().rangeBitwiseAnd(5, 7))
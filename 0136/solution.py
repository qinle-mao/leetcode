class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from functools import reduce
        return reduce(lambda x, y : x ^ y, nums)

nums = [2, 1, 1]
print(Solution().singleNumber(nums))
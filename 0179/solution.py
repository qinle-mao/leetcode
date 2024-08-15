class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def isLess(a, b):
            x = str(a) + str(b)
            y = str(b) + str(a)
            return x < y
        
        for i in range(1, len(nums)):
            currNum, j = nums[i], 0
            for j in range(i, -1, -1):
                if isLess(currNum, nums[j-1]):
                    break
                nums[j] = nums[j-1]
            nums[j] = currNum
        
        while len(nums) > 1:
            if nums[0] == 0:
                nums.pop(0)
            else:
                break
        res = ''
        
        for e in nums:
            res += str(e)
        return res

nums = [3,30,34,5,9]
print(Solution().largestNumber([0, 0, 0, 0]))
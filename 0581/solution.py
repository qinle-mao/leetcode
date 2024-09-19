class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        newNums = sorted(nums)
        left, right = 0, n - 1
        while left < n and newNums[left] == nums[left]:
            left += 1
        while right > left and newNums[right] == nums[right]:
            right -= 1
        if left < right:
            return right - left + 1
        return 0
    
    def findUnsortedSubarray2(self, nums):
        n = len(nums)
        maxNum, right = float('-inf'), -1
        minNum, left = float('inf'), -1
        for i in range(n):
            if maxNum > nums[i]:
                right = i
            else:
                maxNum = nums[i]
            if minNum < nums[n - i - 1]:
                left = n - i - 1
            else:
                minNum = nums[n - i - 1]
        return 0 if right == -1 else right - left + 1

nums = [2,6,4,8,10,9,15]
print(Solution().findUnsortedSubarray2(nums))
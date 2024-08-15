class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(len(nums), float('-inf'))
        nums.insert(0, float('-inf'))
        diff = [nums[0]-nums[1]]
        for i in range(1, len(nums)-1):
            diff.append(nums[i] - nums[i+1])
            if diff[i-1] < 0 and diff[i] > 0:
                return i - 1
        return len(nums) - 2

    # binary search
    def findPeakElement2(self, nums):
        nums.insert(len(nums), float('-inf'))
        nums.insert(0, float('-inf'))
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid - 1
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return len(nums) - 2

nums = [1, 2, 3, 1]
print(Solution().findPeakElement2(nums))
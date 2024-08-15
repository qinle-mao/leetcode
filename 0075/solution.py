# Sorting
class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            curr_num = nums[i]
            j = i
            while j > 0 and curr_num < nums[j-1]:
                nums[j] = nums[j-1]
                j -= 1
            nums[j] = curr_num
        return nums

nums = [2,0,2,1,1,0]
print(Solution().sortColors(nums))            
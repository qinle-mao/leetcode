class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left, right =-1, 0 # exclusive left, exclusive right
        sum = 0
        res = float('inf')
        while left < right:
            if sum >= target:
                res = min(res, right - left - 1)
                left += 1
                sum -= nums[left]
            elif right < n: 
                sum += nums[right]
                right += 1
            else:
                break
        if res == float('inf'):
            return 0
        return res

# target, nums = 7, [2,3,1,2,4,3]
target, nums = 15, [5,1,3,5,10,7,4,9,2,8]
print(Solution().minSubArrayLen(target, nums))
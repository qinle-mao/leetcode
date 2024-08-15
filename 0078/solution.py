class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def step(arr, i, res):
            if i == len(nums):
                res.append(arr)
                return
            step(arr+[nums[i]], i+1, res)
            step(arr, i+1, res)
        res = []
        step([], 0, res)
        return res

nums = [0]
print(Solution().subsets(nums))
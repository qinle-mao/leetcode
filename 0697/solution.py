class Solution(object):
    def findShortestSubArray(self, nums):
        arr = [0] * 50000
        max_count = 0
        for e in nums:
            arr[e] += 1
            max_count = max(arr[e], max_count)
        arr_1 = []
        for i in range(len(arr)):
            if arr[i] == max_count:
                arr_1.append(i)
        res = len(nums)
        for e in arr_1:
            for i in range(0, len(nums)):
                if(nums[i] == e):
                    break
            for j in range(0, len(nums)):
                if(nums[len(nums)-1-j] == e):
                    break
            res = min(len(nums)-i-j, res)
        return res

nums = [1,1,2,2,2,1]
# nums = [2,1,1,2,1,3,3,3,1,3,1,3,2]
print(Solution.findShortestSubArray(Solution(), nums))
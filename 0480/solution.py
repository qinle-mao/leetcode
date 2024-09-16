class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        def getMedian(arr, k):
            if k % 2 == 0:
                return float(arr[k//2-1] + arr[k//2]) / 2
            else:
                return float(arr[k//2])
        
        def remove(arr, val):
            def step(left, right):
                if left > right:
                    return
                mid = (left + right) // 2
                if arr[mid] == val:
                    arr.pop(mid)
                elif arr[mid] > val:
                    step(left, mid - 1)
                else:
                    step(mid + 1, right)
            step(0, len(arr)-1)
        
        def insert(arr, val):
            def step(left, right):
                if left > right:
                    arr.insert(left, val)
                    return
                mid = (left + right) // 2
                if arr[mid] == val:
                    arr.insert(mid, val)
                elif arr[mid] > val:
                    step(left, mid - 1)
                else:
                    step(mid + 1, right)
            step(0, len(arr)-1)
        
        n = len(nums)
        if n < k:
            return []
        res = []
        arr = sorted(nums[:k])
        res.append(getMedian(arr, k))
        for i in range(1, n - k + 1):
            remove(arr, nums[i-1])
            insert(arr, nums[i+k-1])
            res.append(getMedian(arr, k))
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
# nums = [1,4,2,3]
# k = 4
print(Solution().medianSlidingWindow(nums, k))
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        from sortedcontainers import SortedList
        window = SortedList()
        for i in range(len(nums)):
            # len(window) == k
            if i > indexDiff:
                window.remove(nums[i - 1 - indexDiff])
            window.add(nums[i])
            idx = window.bisect_left(nums[i])
            if idx > 0 and abs(window[idx] - window[idx-1]) <= valueDiff:
                return True
            if idx < len(window) - 1 and abs(window[idx+1] - window[idx]) <= valueDiff:
                return True
        return False
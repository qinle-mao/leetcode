# nums may contain duplicates
class Solution(object):
    # For the currently selected number x, 
    # if there is a same number y in front of it, and y is not selected, 
    # the subset containing x will inevitably appear in all subsets containing y.
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def step(pos, selected):
            def check():
                for i in range(pos):
                    if nums[i] == nums[pos] and not selected[i]:
                        return True
                return False
            if pos == len(nums):
                print(selected)
                self.res.append([nums[i] for i in range(len(nums)) if selected[i]])
                return
            if not check():
                step(pos + 1, [e for e in selected] + [True])
            step(pos + 1, [e for e in selected] + [False])
        self.res = []
        step(0, [])
        return self.res
        
    def subsetsWithDup2(self, nums):
        def step(pos, arr):
            if pos == len(nums):
                arr = sorted(arr)
                if arr not in self.res:
                    self.res.append(arr)
            else:
                step(pos + 1, [e for e in arr])
                step(pos + 1, [e for e in arr] + [nums[pos]])
        self.res = []
        step(0, [])
        return self.res

nums = [1, 2, 2]
print(Solution().subsetsWithDup(nums))
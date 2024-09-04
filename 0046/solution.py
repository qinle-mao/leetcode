class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def step(currRes, currRemain):
            n = len(currRemain)
            if n == 0:
                self.res.append(currRes)
                return
            for i in range(n):
                newRes = [_ for _ in currRes] + [currRemain[i]]
                newRemain = [_ for _ in currRemain]
                newRemain.pop(i)
                step(newRes, newRemain)
        
        self.res = []
        step([], nums)
        return self.res

nums = [1,2,3] # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permute(nums))
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def step(arr, currLen, currMin, res):
            if currLen == k:
                if sum(arr) == n:
                    res.append([e for e in arr])
                return
            for x in range(currMin, 10):
                step([e for e in arr] + [x], currLen + 1, x + 1, res)

        arr = []     
        res = []
        step(arr, 0, 1, res)
        return res        

k, n = 3, 9
print(Solution().combinationSum3(k, n))
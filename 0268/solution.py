class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0] * (len(nums) + 1)
        for n in nums:
            count[n] = 1
        for i in range(len(count)):
            if count[i] == 0:
                return i
    
    # get sum

    # bit operations
    def missingNumber2(self, nums):
        xor = 0
        for i, num in enumerate(nums):
            xor ^= i ^ num
        return xor ^ len(nums)
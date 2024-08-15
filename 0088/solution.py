class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        res = []
        pos1 = pos2 = 0
        while pos1 < m and pos2 < n:
            if nums1[pos1] <= nums2[pos2]:
                res.append(nums1[pos1])
                pos1 += 1
            else:
                res.append(nums2[pos2])
                pos2 += 1
        res += nums1[pos1:m] + nums2[pos2:n]
        nums1[:] = res # do not point to a new list

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)
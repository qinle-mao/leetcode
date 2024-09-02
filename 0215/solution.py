class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        def percDown(pos, n):
            while pos < n:
                child = -1
                leftChild, rightChild = pos * 2 + 1, pos * 2 + 2
                if leftChild >= n:
                    break
                elif rightChild >=n or nums[leftChild] > nums[rightChild]:
                    child = leftChild
                else:
                    child = rightChild
                if nums[pos] < nums[child]:
                    swap(pos, child)
                    pos = child
                else:
                    break

        n = len(nums)
        # building max heap
        for i in range(n//2, -1, -1):
            percDown(i, n)
        # delete max
        for i in range(k-1):
            heapLen = n - 1 - i
            swap(0, heapLen)
            percDown(0, heapLen)
        return nums[0]
        
nums = [2, 1]
k = 2
print(Solution().findKthLargest(nums, k))
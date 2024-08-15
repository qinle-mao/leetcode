class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        for i in range(len(citations)):
            if h < citations[len(citations)-1-i]:
                h += 1
            else:
                break
        return h

    # binary search - find i where A[i] == len(A) - i given a sorted array A
    def hIndex_2(self, citations):
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= len(citations) - mid:
                right = mid - 1
            else:
                left = mid + 1
        return len(citations) - left
    
citations_1 = [0, 1, 3, 5, 6]
citations_2 = [1, 2, 100]
citations_3 = [1]
print(Solution().hIndex_2(citations=citations_1))
print(Solution().hIndex_2(citations=citations_2))
print(Solution().hIndex_2(citations=citations_3))
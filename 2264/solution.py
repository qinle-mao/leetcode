class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        left, right = 0, 0
        maxN = -1
        while right < len(num):
            if right - left == 3:
                maxN = max(maxN, int(num[left]))
                left = right
            elif num[right] == num[left]:
                right += 1
            else:
                left += 1
                right = left
        if right - left == 3:
            maxN = max(maxN, int(num[left]))
        if maxN == -1:
            return ''
        else:
            return str(maxN) * 3

# num = '6777133339'
num = '42352338'
# num = '333666'
# num = '222'
print(Solution().largestGoodInteger(num))
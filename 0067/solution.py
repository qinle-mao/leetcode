class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def get(str, i):
            if i >= -len(str):
                return int(str[i])
            else:
                return 0
        
        sum = []
        carry = 0
        i = -1
        while i >= -len(a) or i >= -len(b) or carry != 0:
            currSum = get(a, i) + get(b, i) + carry
            if currSum >= 2:
                currSum -= 2
                carry = 1
            else:
                carry = 0
            sum.insert(0, str(currSum))
            i -= 1
        return ''.join(sum)

a = '11'
b = '1'
print(Solution().addBinary(a, b))
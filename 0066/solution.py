class Solution(object):
    def plusOne(self, digits):
        carry = 1
        res = []
        for i in range(len(digits)):
            curr = digits[len(digits)-i-1] + carry
            if curr > 9:
                carry = 1
                curr -= 10
            else:
                carry = 0
            res.insert(0, curr)
        if carry == 1:
            res.insert(0, 1)
        return res

digits = [1,2,3]
print(Solution().plusOne(digits))
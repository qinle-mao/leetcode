class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

n = 0b00000010100101000001111010011100
print(Solution().reverseBits(n))
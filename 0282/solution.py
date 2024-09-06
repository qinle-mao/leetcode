class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def step(idx, s, sum, lastNum, lastOp, lastMulRes):
            if idx > n - 2:
                if sum == target:
                    res.append(s)
                return
            digit = num[idx+1]
            # '' (no operator)
            if lastNum != 0:
                if lastNum > 0:
                    newLastNum = lastNum * 10 + float(digit)
                else:
                    newLastNum = lastNum * 10 - float(digit)
                if lastOp == '+':
                    newSum = sum - lastNum + newLastNum
                    step(idx + 1, s + digit, newSum, newLastNum, '+', newLastNum)
                elif lastOp == '-':
                    newSum = sum - lastNum + newLastNum
                    step(idx + 1, s + digit, newSum, newLastNum, '-', newLastNum)
                elif lastOp == '*':
                    newLastMulRes = lastMulRes // lastNum * newLastNum
                    newSum = sum - lastMulRes + newLastMulRes
                    step(idx + 1, s + digit, newSum, newLastNum, '*', newLastMulRes)
                # elif lastOp == '/':
                #     newLastMulRes = lastMulRes * lastNum // newLastNum
                #     newSum = sum - lastMulRes + newLastMulRes
                #     step(idx + 1, s + digit, newSum, newLastNum, '/', newLastMulRes)
            # '+'
            step(idx + 1, s + '+' + digit, sum + float(digit), float(digit), '+', float(digit))
            # '-'
            step(idx + 1, s + '-' + digit, sum - float(digit), -float(digit), '-', -float(digit))
            # '*'
            newMulRes = lastMulRes * float(digit)
            newSum = sum - lastMulRes + newMulRes
            step(idx + 1, s + '*' + digit, newSum, float(digit), '*', newMulRes)
            # '/'
            # if float(digit) != 0:
            #     newMulRes = lastMulRes // float(digit)
            #     newSum = sum - lastMulRes + newMulRes
            #     step(idx + 1, s + '/' + digit, newSum, float(digit), '/', newMulRes)
        
        n = len(num)
        res = []
        step(0, num[0], float(num[0]), float(num[0]), '+', float(num[0]))
        return res

# num, target = '123', 6
# num, target = '23201', 7
# num, target = '345', 15
# num, target = '3456237490', 9191
num, target = '123456789', 45
print(Solution().addOperators(num, target))
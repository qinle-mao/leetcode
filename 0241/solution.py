class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def step(left, right):
            if left == right:
                return [int(ops[left])]
            res = []
            for i in range(left, right, 2):
                leftRes = step(left, i)
                rightRes = step(i + 2, right)
                for a in leftRes:
                    for b in rightRes:
                        if ops[i+1] == '+':
                            res.append(a + b)
                        elif ops[i+1] == '-':
                            res.append(a - b)
                        else:
                            res.append(a * b)
            return res
        ops = []
        i, n = 0, len(expression)
        while i < n:
            if expression[i].isdigit():
                num = 0
                while i < n and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                ops.append(str(num))
            else:
                ops.append(expression[i])
                i += 1
        return step(0, len(ops) - 1)
    
expression = '2*3-4*5'
print(Solution().diffWaysToCompute(expression))
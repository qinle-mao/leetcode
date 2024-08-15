class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def getDivision(a, b):
            if a * b >= 0:
                return a // b
            else:
                return -(abs(a) // abs(b))
        stack = []
        for i in range(len(tokens)):
            currS = tokens[i]
            if currS == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif currS == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif currS == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif currS == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(getDivision(a, b))
            else:
                stack.append(int(currS))
        return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))        
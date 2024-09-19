class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def getFraction(i):
            flag = 1
            if expression[i] == '-':
                flag *= -1
            if i > 0 or expression[i] == '-':
                i += 1
            n = len(expression)
            numerator = denominator = 0
            while '0' <= expression[i] <= '9':
                numerator = numerator * 10 + int(expression[i])
                i += 1
            i += 1
            while i < n and '0' <= expression[i] <= '9':
                denominator = denominator * 10 + int(expression[i])
                i += 1
            return flag * numerator, denominator, i
        
        def reduce(numerator, denominator):
            if numerator == 0:
                return 0, 1
            minNum = min(abs(numerator), abs(denominator))
            for factor in range(2, minNum // 2 + 1):
                while numerator % factor == 0 and denominator % factor == 0:
                    numerator //= factor
                    denominator //= factor
            return numerator, denominator

        def addFraction(res, numerator1, denominator1):
            if res['numerator'] == res['denominator'] == 0:
                res['numerator'], res['denominator'] = reduce(numerator1, denominator1)
                return
            numerator2, denominator2 = res['numerator'], res['denominator']
            numeratorNew = numerator1 * denominator2 + numerator2 * denominator1
            denominatorNew = denominator1 * denominator2
            res['numerator'], res['denominator'] = reduce(numeratorNew, denominatorNew)
        
        i, n = 0, len(expression)
        res = {'numerator': 0, 'denominator': 0}
        while i < n:
            numerator, denominator, i = getFraction(i)
            addFraction(res, numerator, denominator)
        return str(res['numerator']) + '/' + str(res['denominator'])

expression = '-1/4-4/5-1/4'
print(Solution().fractionAddition(expression))
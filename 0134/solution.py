class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        i = 0
        while i < n:
            sumOfGas, sumOfCost = 0, 0
            count = 0
            while count < n:
                j = (i + count) % n
                sumOfGas += gas[j]
                sumOfCost += cost[j]
                if sumOfCost > sumOfGas:
                    break
                count += 1
            if count == n:
                return i
            else:
                i += (count + 1) # important !
        return -1

    # outside time limit
    def canCompleteCircuit2(self, gas, cost):
        n = len(gas)
        arr = [gas[i] - cost[i] for i in range(n)]
        for i in range(n):
            sum = 0
            flag = 1
            for j in range(n):
                sum += arr[(i + j) % n]
                if sum < 0:
                    flag = 0
                    break
            if flag == 1:
                return i
        return -1

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        timeSeries.append(float('inf'))
        totalTime = 0
        currTime = timeSeries[0]
        for i in range(1, len(timeSeries)):
            newTime = timeSeries[i]
            if newTime - currTime > duration:
                totalTime += duration
            else:
                totalTime += newTime - currTime
            currTime = newTime
        return totalTime

timeSeries, duration = [1,4], 2
print(Solution().findPoisonedDuration(timeSeries, duration))
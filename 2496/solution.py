class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [round(kelvin, 5), round(fahrenheit, 5)]

celsius = 36.50
print(Solution().convertTemperature(celsius))
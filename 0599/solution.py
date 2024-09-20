class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dictionary = {}
        for i in range(len(list1)):
            dictionary[list1[i]] = i
        res, minSum = [], float('inf')
        for i in range(len(list2)):
            currStr = list2[i]
            if currStr in dictionary.keys():
                currSum = dictionary[currStr] + i
                if currSum < minSum:
                    minSum = currSum
                    res[:] = [currStr]
                elif currSum == minSum:
                    res.append(currStr)
        return res

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(Solution().findRestaurant(list1, list2))
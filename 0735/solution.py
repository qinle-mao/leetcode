class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            if len(stack) == 0 or asteroid > 0 or asteroid * stack[-1] > 0:
                stack.append(asteroid)
            else:
                flag = 0
                while len(stack) > 0:
                    top = stack[-1]
                    if top + asteroid == 0:
                        flag = 1
                        stack.pop()
                        break
                    elif top + asteroid > 0:
                        flag = 1
                        break
                    elif top * asteroid > 0:
                        break
                    else:
                        stack.pop()
                if flag == 0:
                    stack.append(asteroid)
        return stack
    
# asteroids = [5,10,-5]
# asteroids = [8,-8]
asteroids = [10,2,-5]
# asteroids = [-2,-1,1,2]
# asteroids = [-2,-2,1,-2]
print(Solution().asteroidCollision(asteroids))
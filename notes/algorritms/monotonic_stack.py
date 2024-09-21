# Commonly used to efficiently solve problems such as finding the next greater or smaller element in an array etc.
def monoIncreasing(nums):
    stack = []
    res = []
    for num in nums:
        while len(stack) > 0 and stack[-1] > num:
            stack.pop()
        stack.append(num)
    while len(stack) > 0:
        res.insert(0, stack.pop())

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(monoIncreasing(nums))
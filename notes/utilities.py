# infinity
print(float('inf'))
print(float('-inf'))

# str <-> int
print(ord('a')) # 97
print(chr(97)) # 'a'

# round a float nunmber
print(round(12.6667, 3)) # 12.667

# lambda - anonymous functions
# f = lambda arguments : expression(return value)
f = lambda : 'Hello wolrd!'
print(f()) # 'Hello wolrd!'
g = lambda a, b : a + b + 10
print(g(5, 8)) # 23
# reduce() / map() / filter() for lambda
nums = [1, 2, 3, 4, 5]
from functools import reduce
print(reduce(lambda x, y : x * y, nums)) # 20 (1*2*3*4*5)
print(list(map(lambda x : x ** 2, nums))) # [1, 4, 9, 16, 25]
print(list(filter(lambda x : x % 2 == 0, nums))) # [2, 4]

# PriorityQueue - minheap (maxheap not supported)
from queue import PriorityQueue
heap = PriorityQueue()
heap.put(3)
heap.put(1)
heap.put(4)
heap.put(2)
print(heap.get()) # 1
print(heap.get()) # 2
print(heap.get()) # 3
print(heap.get()) # 4
# heapq - minheap (maxheap not supported)
import heapq
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
print(heap) # [1, 5, 3]
heapq.heappop(heap)
print(heap) # [3, 5]

# math lib - gcd()
import math
print(math.gcd(104, 80)) # greatest common divisor - 8

# defaultdict
from collections import defaultdict
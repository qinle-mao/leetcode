class SegmentTreeSum(object):
    def __init__(self, arr):
        def build(pos):
            if pos >= len(self.vals):
                return 0
            left, right = pos * 2 + 1, pos * 2 + 2
            self.vals[pos] += build(left) + build(right)
            return self.vals[pos]
        self.vals = [0 for _ in range(len(arr) * 2 - 1)]
        for i in range(len(arr)):
            self.vals[len(arr)-1+i] = arr[i]
        build(0)
    
    def __str__(self):
        return str(self.vals)
    
    def update(self, pos, val):
        pass

class SegmentTreeMax(object):
    def __init__(self, arr):
        def build(pos):
            if pos >= len(self.vals):
                return float('-inf')
            left, right = pos * 2 + 1, pos * 2 + 2
            self.vals[pos] = max(self.vals[pos], build(left), build(right))
            return self.vals[pos]
        self.vals = [0 for _ in range(len(arr) * 2 - 1)]
        for i in range(len(arr)):
            self.vals[len(arr)-1+i] = arr[i]
        build(0)
    
    def __str__(self):
        return str(self.vals)
    
    def update(self, pos, val):
        pass

#       60 
#    33     27
#  21   12 13 14
# 10 11
tree = SegmentTreeSum([12, 13, 14, 10, 11])
print(tree)
#       14 
#    12     14
#  11   12 13 14
# 10 11
tree = SegmentTreeMax([12, 13, 14, 10, 11])
print(tree)
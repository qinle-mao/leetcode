class Solution(object):
    # sorting + double pointers + greedy
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        m, n = len(g), len(s)
        i = j = count = 0
        while i < m and j < n:
            while j < n and g[i] > s[j]:
                j += 1
            if j < n:
                count += 1
            i += 1
            j += 1
        return count
    
    # exceeding time limit
    def findContentChildren2(self, g, s):
        def buildMaxHeap(arr):
            def swap(i, j):
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            def percDown(pos, n):
                while pos < n:
                    child = -1
                    left, right = pos * 2 + 1, pos * 2 + 2
                    if left >= n:
                        break
                    elif right >= n or arr[left] > arr[right]:
                        child = left
                    else:
                        child = right
                    if arr[pos] < arr[child]:
                        swap(pos, child)
                        pos = child
                    else:
                        break
            n = len(arr)
            for i in range(n//2, -1, -1):
                percDown(i, n)
        
        def instertCookie(cookie, cookieList, g):
            def getCount(pos, n):
                if pos >= n:
                    return 0
                count = getCount(pos * 2 + 1, n) + getCount(pos * 2 + 2, n)
                if cookie >= g[pos]:
                    count += 1
                return count

            count = getCount(0, len(g))
            cookieList.append([cookie, count])
            cookieList.sort()

        buildMaxHeap(g)
        cookieList = []
        for cookie in s:
            instertCookie(cookie, cookieList, g)
        res = 0
        for i in range(len(cookieList)):
            if cookieList[i][1] > 0:
                res += 1
                for j in range(i + 1, len(cookieList)):
                    cookieList[j][1] -= 1
        return res

g = [10,9,8,7]
s = [5,6,7,8]
print(Solution().findContentChildren(g, s))
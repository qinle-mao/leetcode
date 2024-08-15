# Graph - Breadth First Search
class Solution(object):
    def findLadders_1(self, beginWord, endWord, wordList):
        from collections import deque
        def check(a, b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            if count == 1:
                return True
            else:
                return False
        def createGraph(array):
            graph = {}
            for i in range(len(array)):
                graph[array[i]] = []
            for i in range(len(array)):
                for j in range(i+1, len(array)):
                    if check(array[i], array[j]):
                        graph[array[i]].append(array[j])
                        graph[array[j]].append(array[i])
            return graph

        def bfs(graph, beginWord, endWord):
            res = []
            q = deque()
            visited = {}
            for word in graph.keys():
                visited[word] = 0
            
            q.append(beginWord)
            while q:
                currWord = q.popleft()
                visited[currWord] = 1
                res.append(currWord)
                for neighbor in graph[currWord]:
                    if visited[neighbor] == 0:
                        q.append(neighbor)
            
            return res
        
        if endWord not in wordList:
            return []
        if beginWord not in wordList:
            wordList.append(beginWord)
        graph =createGraph(wordList)
        # TODO



    # Dijkstra - exceed time limit
    def findLadders_2(self, beginWord, endWord, wordList):
        from copy import deepcopy
        INFINITY = 600

        def check(a, b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            if count == 1:
                return True
            else:
                return False
        def createGraph(array):
            graph = {}
            for i in range(len(array)):
                graph[array[i]] = []
            for i in range(len(array)):
                for j in range(i+1, len(array)):
                    if check(array[i], array[j]):
                        graph[array[i]].append(array[j])
                        graph[array[j]].append(array[i])
            return graph
        
        def findMinPos(process):
            array = [pos for pos in process.keys() if process[pos]['done'] == 0]
            minDist = INFINITY
            minPos = None
            for pos in array:
                if process[pos]['dist'] < minDist:
                    minDist = process[pos]['dist']
                    minPos = pos
            return minPos
        def dikjstra(graph, begin, end):
            process = {}
            keys = list(graph.keys())
            for i in range(len(keys)):
                process[keys[i]] = {'dist':INFINITY, 'done':0, 'path':[[]]}
            process[begin]['dist'] = 0
            while True:
                tmp = findMinPos(process)
                if tmp == None:
                    break
                process[tmp]['done'] = 1
                for path in process[tmp]['path']:
                        path.append(tmp)
                for pos in graph[tmp]:
                    if process[pos]['done'] == 0:
                        currDist = process[pos]['dist']
                        newDist = process[tmp]['dist'] + 1
                        if newDist < currDist:
                            process[pos]['dist'] = newDist
                            process[pos]['path'] = deepcopy(process[tmp]['path'])
                        elif newDist == currDist:
                            process[pos]['path'] += deepcopy(process[tmp]['path'])
            res = process[end]['path']
            if res == [[]]:
                res = []
            return res
        
        if endWord not in wordList:
            return []
        if beginWord not in wordList:
            wordList.append(beginWord)
        graph =createGraph(wordList)
        return dikjstra(graph, beginWord, endWord)

beginWord_1 = 'hit'
endWord_1 = 'cog'
wordList_1 = ['hot','dot','dog','lot','log','cog']

beginWord_2 = 'hot'
endWord_2 = 'dog'
wordList_2 = ['hot','dog']

beginWord_3 = 'qa'
endWord_3 = 'sq'
wordList_3 = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti",
            "ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc",
            "lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di",
            "hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io",
            "be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

f = open('output', 'w')
f.write(str(Solution().findLadders_1(beginWord=beginWord_3, endWord=endWord_3, wordList=wordList_3)))
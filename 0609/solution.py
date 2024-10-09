class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        def getContent(file):
            name, content = '', ''
            pos = 0
            while file[pos] != '(':
                name += file[pos]
                pos += 1
            pos += 1
            while file[pos] != ')':
                content += file[pos]
                pos += 1
            return name, content
        
        res = []
        hashMap = defaultdict(list)
        for directory in paths:
            tmp = directory.split()
            root, files = tmp[0], tmp[1:]
            for file in files:
                name, content = getContent(file)
                hashMap[content].append(root + '/' + name)
        for _, arr in hashMap.items():
            if len(arr) > 1:
                res.append(arr)
        return res

paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
print(Solution().findDuplicate(paths))
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        status = 0 # 0 - outside comment; 1 - inside comment
        newLine = ''
        for line in source:
            if status == 0:
                newLine = ''
            pos, n = 0, len(line)
            while pos < n:
                if status == 0:
                    if line[pos:pos+2] == '/*':
                        status = 1
                        pos += 2
                    elif line[pos:pos+2] == '//':
                        break
                    else:
                        newLine += line[pos]
                        pos += 1
                else:
                    if line[pos:pos+2] == '*/':
                        status = 0
                        pos += 2
                    else:
                        pos += 1
            if status == 0 and newLine != '':
                res.append(newLine)
        return res

source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
# source = ["a/*comment", "line", "more_comment*/b"]
print(Solution().removeComments(source))
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        leng1 = len(s1)
        leng2 = len(s2)
        if leng1 + leng2 != len(s3):
            return False

        cursor = set([(0, 0)])
        for s3char in s3:
            cursorList = set()
            isS1 = False
            isS2 = False

            for n, m in cursor:
                print(n, m)
                if n < leng1 and s1[n] == s3char:
                    cursorList.add((n+1, m))
                    isS1 = True
                if m < leng2 and s2[m] == s3char:
                    cursorList.add((n, m+1))
                    isS2 = True
            if not cursorList:
                return False

            cursor = cursorList

        return True
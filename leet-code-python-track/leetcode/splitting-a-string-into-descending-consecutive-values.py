class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def search(i,parent):
            if i==n:
                return True
            for o in range(i+1,n+1):
                if parent==int(s[i:o])+1:
                    if search(o,int(s[i:o])):
                        return True
            return False
        for k in range(1, n):
            if search(k,int(s[:k])):
                return True
        return False
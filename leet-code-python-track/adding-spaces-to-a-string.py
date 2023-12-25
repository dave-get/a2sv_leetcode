class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        k=""
        a=0
        for i in spaces:  
            k+=s[a:i]
            k+=" "
            a=i
        k+=s[a:]
        return k

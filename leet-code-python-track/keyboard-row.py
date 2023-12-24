class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a="qwertyuiop"
        b="asdfghjkl"
        c="zxcvbnm"
        lis=[]
        for word in words:
            cn1=0
            cn2=0
            cn3=0
            for char in word:
                if char.lower() in a:
                    cn1+=1
                if char.lower() in b:
                    cn2+=1
                if char.lower() in c:
                    cn3+=1
            if cn1==0 and cn2==0:
                lis.append(word)
            if cn2==0 and cn3==0:
                lis.append(word)
            if cn1==0 and cn3==0:
                lis.append(word)
        return lis

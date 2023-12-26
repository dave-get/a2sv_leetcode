class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        s=max(words,key=len)
        sas=len(s)
        for i in range(sas):
            c_t=1
            t=True
            y="same"
            for j in range(len(words)-1):
                if i<len(words[j]):
                    a=order.find(words[j][i])
                else:
                    a=-1
                if i<len(words[j+1]):
                    b=order.find(words[j+1][i])
                else:
                    b=-1
                if a==b:
                    y="same"
                elif a < b:
                    y="No"
                    c_t+=1
                else:
                    y="NO"
                    t=False
                    break
            if "same"==y:
                continue
            if t==False:
                return False
                break
            elif c_t == len(words):
                return True
                break
        return True
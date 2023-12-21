class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        out1=""
        out2=""
        m=max(len(word1),len(word2))
        for i in range(m):
            if i<len(word1):
                out1+=word1[i]
            if i<len(word2):
                out2+=word2[i]
        if out1==out2:
            return True
        else:
            return False
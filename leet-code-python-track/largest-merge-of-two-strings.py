class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        s = ""
        while word1 or word2:
            if word1 > word2:
                s += word1[0]
                word1 = word1[1:]
            elif word2 > word1:
                s += word2[0]
                word2 = word2[1:]
            else:
                if word1 > word2:
                    s += word1[0]
                    word1 = word1[1:]
                else:
                    s += word2[0]
                    word2 = word2[1:]
        return s
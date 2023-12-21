class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=""
        max_len = max(len(word1),len(word2))
        for i in range(max_len):
            if len(word1)>i:
                word3 = word3 + word1[i]
            if len(word2)>i:
                word3 = word3 + word2[i]
        return word3
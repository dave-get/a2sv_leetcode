class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left =0
        right =0
        ans_f = ans_t =0
        count_false =0
        while right < len(answerKey):
            if answerKey[right] == "F":
                count_false +=1
            if count_false > k:
                ans_f = max(ans_f,right-left)
                while count_false > k:
                    if answerKey[left] == "F":
                        count_false -=1
                    left +=1
            ans_f = max(ans_f,right-left+1)
            right +=1
        count_true =0
        left =0
        right =0
        while right < len(answerKey):
            if answerKey[right] == "T":
                count_true +=1
            if count_true > k:
                ans_t = max(ans_t,right-left)
                while count_true > k:
                    if answerKey[left] == "T":
                        count_true -=1
                    left +=1
            ans_t = max(ans_t,right-left+1)
            right +=1
        res = max(ans_t,ans_f)
        return res
        
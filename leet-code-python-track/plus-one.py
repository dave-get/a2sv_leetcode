class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in range(len(digits)):
            s+=str(digits[i])
        s=int(s)
        s+=1
        s=str(s)
        Answer=[]
        for i in range(len(s)):
            Answer.append(int(s[i]))
        return Answer
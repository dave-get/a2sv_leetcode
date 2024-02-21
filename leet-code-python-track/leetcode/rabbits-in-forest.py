class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = defaultdict(int)
        count = 0
        for i in range(len(answers)):
            dic[answers[i]] +=1
        for key,val in dic.items():
            if key == 0:
               count +=val
            else:
                a = math.ceil(val/(key+1))
                count +=a*(key+1) 
        return count

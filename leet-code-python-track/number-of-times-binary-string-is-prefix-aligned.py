class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        list_ = []
        sum_ =0
        for num in flips:
            sum_ +=num
            list_.append(sum_)
        flips.sort()
        for i in range(len(flips)):
            calc = ((i+1)/2)*(flips[0]+flips[i])
            if calc == list_[i]:
                count +=1
        return count
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        lis = []
        for i in range(1,len(weights)):
            lis.append(weights[i] + weights[i-1])
        lis.sort()
        l =len(lis)-1
        min_=max_ =0
        for i in range(k-1):
            min_ +=lis[i]
            max_ +=lis[l]
            l -=1
        return max_ - min_
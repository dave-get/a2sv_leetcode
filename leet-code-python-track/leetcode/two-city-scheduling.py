class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        lis = []
        for i in range(len(costs)):
            lis.append((costs[i][0] - costs[i][1]))
        for i in range(1,len(costs)):
            k = i
            while k >= 1 and lis[k] < lis[k-1]:
                lis[k],lis[k-1] = lis[k-1],lis[k]
                costs[k],costs[k-1] = costs[k-1],costs[k]
                k -=1
        l = len(costs)//2
        sum_ = 0
        for i in range(l):
            sum_ += costs[i][0] + costs[i+l][1]
        return sum_


            
        
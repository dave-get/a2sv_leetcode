class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        stop = target
        remender = 0
        count_double_use = 0
        double = maxDoubles
        while stop > 2 and maxDoubles > 0:
            remender += target%2
            stop = target//2
            target = target//2
            count_double_use +=1
            maxDoubles -=1
        if double == 0:   
            return target -1
        else:
            ans = remender + stop -1 + count_double_use
            return ans
            

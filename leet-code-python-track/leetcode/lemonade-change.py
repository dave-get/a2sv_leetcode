class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dic = defaultdict(int)
        for i in range(len(bills)):
            if bills[i] == 10:
                if dic[5] > 0:
                    dic[5] -=1
                else:
                    return False
            elif bills[i] == 20: 
                if dic[10] > 0 and dic[5] >0:
                    dic[5] -=1
                    dic[10] -=1
                elif dic[5] > 2:
                    dic[5] -=3
                else:
                    return False 
            dic[bills[i]] +=1   
        return True

            

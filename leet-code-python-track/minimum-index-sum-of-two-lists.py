class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lis={}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:  
                    lis[list1[i]]=i+j
        l=[]
        p=min(lis.values())
        for key, value in lis.items():
            if value == p:
                l.append(key)
        return l
                                    

                                
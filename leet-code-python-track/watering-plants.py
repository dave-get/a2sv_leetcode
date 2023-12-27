class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        lis=[]
        can=capacity
        step = 0
        for i in range(len(plants)-1):
            capacity -=plants[i]
            step+=1
            
            if capacity<plants[i+1]:
                lis.append(step)
                capacity = can
                lis.append(step)
        lis.append(step)
        return sum(lis)+1
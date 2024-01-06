class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ln = len(heights)
        # for i in range(leng):
        #     for j in range(1,leng):
        #         if heights[j-1]<heights[j]:
        #             te = names[j-1]
        #             names[j-1] = names[j]
        #             names[j] = temp
        # return names

        for i in range(ln):
            minIndx = i 
            for j in range(i+1,ln):
                if heights[minIndx]<heights[j]:
                    minIndx = j
            names[minIndx], names[i] = names[i], names[minIndx]
            heights[minIndx],heights[i] = heights[i],heights[minIndx]
        
        return names
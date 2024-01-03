class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans_list = []
        for img in image:
            temp = []
            for j in range(len(image[0])-1,-1,-1):
                if img[j] == 0:
                    temp.append(1)
                else:
                    temp.append(0)
            ans_list.append(temp)
        return ans_list
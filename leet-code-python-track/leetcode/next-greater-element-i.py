class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_ = defaultdict(int)
        stack = []
        for i in range(len(nums2)-1):
            if len(stack)==0:
                stack.append(nums2[i])
            if stack[-1] < nums2[i+1]:
                while  len(stack)!=0 and stack[-1] < nums2[i+1]:
                    dict_[stack[-1]] = nums2[i+1]
                    stack.pop()
            stack.append(nums2[i+1])
        ans = []
        for i in nums1:
            if dict_[i]:
                ans.append(dict_[i])
            else:
                ans.append(-1)
        return ans
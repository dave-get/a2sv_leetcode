class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        pops = []
        ans = [-1]*len(nums)
        for i in range(len(nums)):
            while stack and stack[-1][0] < nums[i]:
                ans[stack[-1][1]] = nums[i]
                pops.append(stack.pop())
            stack.append((nums[i],i))


        left = nums[stack[0][1]:] + nums[:stack[0][1]+1]

        left_stack = []
        left_ans = [-1]*len(left)
        for i in range(len(left)):
            while left_stack and left_stack[-1][0] < left[i]:
                left_ans[left_stack[-1][1]] = left[i]
                left_stack.pop()
            left_stack.append((left[i],i))
        for i in range(stack[0][1],len(nums)):
            ans[i] = left_ans[i-stack[0][1]]
        return ans

        
       
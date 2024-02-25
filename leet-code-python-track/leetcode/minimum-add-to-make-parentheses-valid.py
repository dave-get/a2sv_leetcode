class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        c = 0
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    c +=1
        return c+len(stack)
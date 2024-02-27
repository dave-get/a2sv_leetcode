class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = [""]
        for i in s:
            if i == ".." and stack[-1] != "":
                stack.pop()
            elif i != "" and i != ".." and i != ".":
                stack.append(i)
        if stack[-1] == "":
            stack[-1] = "/"
        ans = "/".join(stack)

        return ans
            
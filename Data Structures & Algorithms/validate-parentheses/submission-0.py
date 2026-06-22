class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            print(c,stack)
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack or not ((c == ")" and stack[-1] == "(") or (c == "}" and stack[-1] == "{") or
                (c == "]" and stack[-1] == "[")) :
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
            
        
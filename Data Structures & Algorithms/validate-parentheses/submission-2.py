class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []

        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for j in s:
            if j in pairs:
                if stack and stack[-1] == pairs[j]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(j)
                
        if stack:
            return False
        else:
            return True






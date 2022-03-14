class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return 0
        
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            if i ==")":
                if len(stack)>0 and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False
            if i =="}":
                if len(stack)>0 and stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
                
            if i =="]":
                if len(stack)>0 and stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False
            
        
        if len(stack) == 0:
            return True
        else: return False
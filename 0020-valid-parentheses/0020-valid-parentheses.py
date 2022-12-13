class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s) : # if null return false
            return False
        
        stack = []
        for i in s:
            if i in ["(", "{", "["]:# if i is an open bracket append it in stack
                stack.append(i)
                continue
            
            # if i is a close bracket
            if i ==")":
                # if stack is empty or stack last element is not same
                if not stack or stack.pop() != "(":
                    return False

            elif i =="}":
                # if stack is empty or stack last element is not same
                if not stack or stack.pop() != "{":
                    return False
                
            elif i =="]":
                # if stack is empty or stack last element is not same
                if not stack or stack.pop() != "[":
                    return False
            
        return not len(stack)
            
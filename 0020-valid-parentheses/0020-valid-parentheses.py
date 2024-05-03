class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpen = {"}" : "{", 
                       ")" : "(", 
                       "]" : "["}
                
        for c in s:
            if c in closeToOpen: # if this char is a closing bracket (every key of map is always a closing bracket)
                if stack and stack[-1] == closeToOpen[c]: # make sure stack is not empty and value at the top is the matching opening bracket
                    stack.pop()
                else:
                    return False
            else: # if c is an open bracket
                stack.append(c)
                         
        return True if not stack else False
            
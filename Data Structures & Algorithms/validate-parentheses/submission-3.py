class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
                if not s :
                    return False 
                if s[i] in '({[':
                    stack.append(s[i])

                elif s[i] in ')}]' and not stack:
                    return False
                
                elif s[i] == '}' :
                    if stack.pop() != '{' :
                        return False 
                elif s[i] == ')' :
                    if stack.pop() != '(' :
                        return False
                elif s[i] == ']' :
                    if stack.pop() != '[' :
                        return False
        if stack :
                return False    
        return True
                
            

            
            

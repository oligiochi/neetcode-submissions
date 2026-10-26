class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        Dpar={
            '(':')',
            '[':']',
            '{':'}',
        }
        for c in s:
            if c in Dpar:
               stack.append(c)
            else:
                if not stack:
                    return False
                popC=stack.pop()
                if Dpar[popC]!=c:
                    return False
        
        return not bool(stack)
        
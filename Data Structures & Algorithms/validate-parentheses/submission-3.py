class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={
            '(':')',
            '[':']',
            '{':'}',
        }
        for c in s:
            if c in pairs:
               stack.append(c)
            else:
                if not stack:
                    return False
                popC=stack.pop()
                if pairs[popC]!=c:
                    return False
        
        return not stack
        
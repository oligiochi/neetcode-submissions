class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mappatura={}
        for i in range(len(s)):
            mappatura[s[i]] = mappatura.get(s[i], 0) + 1
            mappatura[t[i]] = mappatura.get(t[i], 0) - 1
        for m in mappatura.values():
            print(m)
            if m!=0:
                return False
        return True
            
        
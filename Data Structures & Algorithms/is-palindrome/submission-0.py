import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl=s.lower()
        ssl=sl.translate(str.maketrans("","",string.punctuation+" "))
        print(ssl)
        return True if ssl==ssl[::-1] else False
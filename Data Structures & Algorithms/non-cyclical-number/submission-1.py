class Solution:
    def isHappy(self, n: int) -> bool:
        resoult = set()
        
        while n != 1 and n not in resoult:
            resoult.add(n)
            n = sum(int(digit)**2 for digit in str(n))
            
        return n == 1

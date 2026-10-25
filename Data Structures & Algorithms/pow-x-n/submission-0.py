class Solution:
    def myPow(self, x: float, n: int) -> float:
        num,power= x if n>0 else 1/x,n if n>0 else -n
        resoult=1
        for i in range(power):
            resoult*=num
        return resoult
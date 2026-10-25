class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        for i,p in enumerate(prices):
            for j in range(i+1,len(prices)):
                dif=prices[j]-p
                maxi = max(maxi, dif)
        return maxi
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        
        for i in range(1, len(prices)):
            maxPrice = max(maxPrice, prices[i] - prices[i-1] + maxPrice)
        
        return maxPrice
            
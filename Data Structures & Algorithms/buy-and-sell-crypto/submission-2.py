class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        if len(prices) == 1:
            return profit
        for price in prices[1:]:
            if price < min_price:
                min_price = price
                continue
            profit = max(profit, price - min_price)
        
        return profit
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for p in prices:
            if p < lowest:
                lowest = p
            profit = max(profit, p-lowest)
        return profit

    def maxProfit_brute(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy, sell = prices[0], prices[1]
        max_profit = 0
        for p in prices[1:]:
            sell = max(sell, p)
            max_profit = max(max_profit, sell-buy)
            if p < buy:
                buy = min(buy, p)
                sell = float("-inf")
            print(buy, sell, max_profit)
        return max_profit

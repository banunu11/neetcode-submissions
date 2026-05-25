class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        buy = prices[0]

        for sell in prices:
            price = max(price, sell-buy)
            print(buy)
            buy = min(buy, sell)
            print(price, buy, sell)
                
        return price


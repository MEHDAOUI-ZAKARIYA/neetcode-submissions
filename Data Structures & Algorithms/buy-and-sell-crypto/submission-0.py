class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        profit = 0
        sell = 0 
        for buy in range (n) :
            sell = buy + 1
            if prices[buy] == max(prices) :
                sell += 1
                continue 
            while sell < n :
                P = prices[sell] - prices[buy]
                profit = max (profit , P )
                sell += 1
        return profit 




                






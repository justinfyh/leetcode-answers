class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # set profit
        cost = prices[0] # set lowest cost to first price

        for i in prices: # for every price in the array
            if i < cost: # if the price is lower than the lowest price
                cost = i # set new lowest price
            elif i - cost > profit: # otherwise if the profit is higher
                profit = i - cost # set new profit

        return profit # return the profit
        
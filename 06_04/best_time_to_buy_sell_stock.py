'''
Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        BRUTE FORCE: O(N^2)
        max_profit = 0 
        for i in range(len(prices)): 
            buy_price = prices[i]
            for j in range(i+1, len(prices)): 
                sell_price = prices[j]
                if sell_price - buy_price > max_profit: 
                    max_profit = sell_price-buy_price 
        return(max_profit)
        '''
        '''
        BETTER IDEA: 
        
        
        
        initialize min_price, max_profit 
        
        Loop through the prices array
        
        In each loop, 
        calculate the minimum price (buy_price - which always comes before sell_price) 
        calculate current profit (buy_price - current minimum price)
        if current profit is greater than max_profit, set max_profit to current profit  
        '''
        #we know that sell_price-buy_price must be max...this means buy_price must be a minimum 
        min_price = float('inf')
        max_profit = 0 
        for price in prices: 
            
            min_price = min(min_price, price) #in each iteration through prices, we must record the minimum buy price 
            
            curr_profit = price - min_price #price is always going to be >= min_price which may remain the same or change at every iteration 
            max_profit = max(max_profit, curr_profit)
        return(max_profit)

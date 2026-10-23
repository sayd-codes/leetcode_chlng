class Solution(object):
    def maxProfit(self, prices):
    
        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price

            profit = price - minPrice

            if profit > maxProfit:
                maxProfit = profit

        return maxProfit

        """
        :type prices: List[int]
        :rtype: int
        """
        
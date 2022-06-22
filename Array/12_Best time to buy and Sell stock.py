class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        maxProfitUptoPreviousDay = maxProfit = prices[1]-prices[0]
        bestbuyvalue = prices[0] if prices[0]<prices[1] else prices[1]
        for i in range(2,len(prices)):
            maxProfit = max(maxProfitUptoPreviousDay, prices[i] - bestbuyvalue)
            maxProfitUptoPreviousDay = maxProfit
            bestbuyvalue = min(bestbuyvalue,prices[i])
        if maxProfit >0:
            return maxProfit
        else:
            return 0






prices = [7,1,5,3,6,4]
T = Solution()
max = T.maxProfit(prices)
print("/n",max)
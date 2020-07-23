class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices)<1:
            return 0
        mini = prices[0]
        diff = 0
        
        for i in range(0,len(prices)):
            if prices[i]<mini:
                mini = prices[i]
            if (prices[i]-mini)>diff:
                diff = prices[i]-mini
        return diff  

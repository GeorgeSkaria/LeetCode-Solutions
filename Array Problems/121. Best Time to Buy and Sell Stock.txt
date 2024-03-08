class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprofit=0
        for ele in prices:
            minprice=min(minprice,ele)
            maxprofit=max(maxprofit,ele-minprice)
        return maxprofit

       
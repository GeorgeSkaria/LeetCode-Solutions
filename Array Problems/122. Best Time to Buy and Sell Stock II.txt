class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        cur=0
        minm=prices[0]
        for i in range(1,len(prices)):
            minm=min(prices[i],minm)
            cur=max(cur,prices[i]-minm)
            profit+=cur
            if(cur>0):
                minm,cur=prices[i],0
        return profit


#Set first element of array as minimum value
#cur->checks profit at each iteration
#profit->calculates total profit

#1)Loop through the prices starting from the second element.
 2)Update the minimum price (minm) seen so far.
 3)Update the maximum profit (cur) by calculating the difference between the current price and the minimum price encountered.
 4)Accumulate the current maximum profit to the total profit (profit).
 5)If cur>0,it means that we have to adjust the pointers to calculate profit at next situation
	:make current element as minimum element and cur=0

>Time Complexity:
The algorithm has a time complexity of O(n), where n is the number of elements in the prices list. This is because it iterates through the list once.
>Space Complexity:
The algorithm has a space complexity of O(1)




                  
        
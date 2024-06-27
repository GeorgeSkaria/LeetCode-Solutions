class Solution:
    def candy(self, ratings: List[int]) -> int:
        l=len(ratings)
        if l==1:
            return 1
        res=[1]*l
        if(ratings[0]>ratings[1]):
            res[0]+=1
        for i in range(1,l):
            if(ratings[i-1]<ratings[i]):
                    res[i]=res[i-1]+1
        for i in range(l-2,-1,-1):
            if(ratings[i]>ratings[i+1] and res[i]<=res[i+1]):
                    res[i]=res[i+1]+1
        print(res)
        return sum(res)

        
'''
#Initialization:
Calculate the length of ratings.
If there's only one child, return 1 candy as it's the only child.
Initialize res with all elements as 1,indicating each child initially receives one candy.

#Assign Initial Candies:
Check if the first child's rating is higher than the second child.
If true, increment the number of candies for the first child by 1 to ensure fairness.

#First Pass (Left to Right):
Iterate through the ratings list from the second child to the last.
For each child, compare its rating with the previous child's rating.
If the current child's rating is higher than the previous one, assign one more candy than the previous child.

#Second Pass (Right to Left):
Iterate through the ratings list in reverse order from the second last child to the first.
For each child, compare its rating with the next child's rating.
If the current child's rating is higher than the next one and has been assigned fewer or equal candies as the next child, assign one more candy than the next child.
This pass ensures fairness by adjusting the number of candies for higher-rated children to the left of lower-rated ones.        '''